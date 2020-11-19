#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h> 
#include <fstream>
#include <iostream>
#include <iomanip>
#include <string>
#include "Gstar.h"
#include <pluginlib/class_list_macros.h>
PLUGINLIB_EXPORT_CLASS(Gstar_planner::GstarPlannerROS, nav_core::BaseGlobalPlanner)
int value;
int mapSize;
bool* OGM;
static const float INFINIT_COST = INT_MAX; 
float infinity = std::numeric_limits< float >::infinity();
float tBreak;  
int clock_gettime(clockid_t clk_id, struct timespect *tp);
inline vector <int> findFreeNeighborCell (int CellID);
namespace Gstar_planner
{
GstarPlannerROS::GstarPlannerROS()
{
}
GstarPlannerROS::GstarPlannerROS(ros::NodeHandle &nh)
{
  ROSNodeHandle = nh;

}
GstarPlannerROS::GstarPlannerROS(std::string name, costmap_2d::Costmap2DROS* costmap_ros)
{
  initialize(name, costmap_ros);
}
void GstarPlannerROS::initialize(std::string name, costmap_2d::Costmap2DROS* costmap_ros)
{

  if (!initialized_)
  {
    costmap_ros_ = costmap_ros;
    costmap_ = costmap_ros_->getCostmap();
    ros::NodeHandle private_nh("~/" + name);
    originX = costmap_->getOriginX();
    originY = costmap_->getOriginY();
    width = costmap_->getSizeInCellsX();
    height = costmap_->getSizeInCellsY();
    resolution = costmap_->getResolution();
    mapSize = width*height;
    tBreak = 1+1/(mapSize); 
    value =0;
    OGM = new bool [mapSize]; 
    for (unsigned int iy = 0; iy < costmap_->getSizeInCellsY(); iy++)
    {
      for (unsigned int ix = 0; ix < costmap_->getSizeInCellsX(); ix++)
      {
        unsigned int cost = static_cast<int>(costmap_->getCost(ix, iy));
        if (cost == 0)
          OGM[iy*width+ix]=true;
        else
          OGM[iy*width+ix]=false;
      }
    }
    initialized_ = true;
  }
  else
    ROS_WARN("This planner has already been initialized");
}
bool GstarPlannerROS::DoPlan(const geometry_msgs::PoseStamped& start, const geometry_msgs::PoseStamped& goal,
                             std::vector<geometry_msgs::PoseStamped>& plan)
{

  if (!initialized_)
  {
    return false;
  }

  ROS_DEBUG("Got a start: %d, %d, and a goal: %d, %d", start.pose.position.x, start.pose.position.y,goal.pose.position.x, goal.pose.position.y);
  plan.clear();
  if (goal.header.frame_id != costmap_ros_->getGlobalFrameID())
  {
    return false;
  }
  tf::Stamped < tf::Pose > goal_tf;
  tf::Stamped < tf::Pose > start_tf;
  poseStampedMsgToTF(goal, goal_tf);
  poseStampedMsgToTF(start, start_tf);
  float startX = start.pose.position.x;
  float startY = start.pose.position.y;
  float goalX = goal.pose.position.x;
  float goalY = goal.pose.position.y;
  getCorrdinate(startX, startY);
  getCorrdinate(goalX, goalY);
  int startCell;
  int goalCell;
  if (isCellInsideMap(startX, startY) && isCellInsideMap(goalX, goalY))
  {
    startCell = convertToCellIndex(startX, startY);
    goalCell = convertToCellIndex(goalX, goalY);
  }
  else
  {
    ROS_WARN("the start or goal is out of the map");
    return false;
  }
  if (isStartAndGoalCellsValid(startCell, goalCell)){

        vector<int> bestPath;
	bestPath.clear();

    bestPath = RAstarPlanner(startCell, goalCell);
    if ( bestPath.size()>0)
    {

// convert the path

      for (int i = 0; i < bestPath.size(); i++)
      {

        float x = 0.0;
        float y = 0.0;

        int index = bestPath[i];

        convertToCoordinate(index, x, y);

        geometry_msgs::PoseStamped pose = goal;

        pose.pose.position.x = x;
        pose.pose.position.y = y;
        pose.pose.position.z = 0.0;

        pose.pose.orientation.x = 0.0;
        pose.pose.orientation.y = 0.0;
        pose.pose.orientation.z = 0.0;
        pose.pose.orientation.w = 1.0;

        plan.push_back(pose);
      }


	float path_length = 0.0;
	
	std::vector<geometry_msgs::PoseStamped>::iterator it = plan.begin();
	
	geometry_msgs::PoseStamped last_pose;
	last_pose = *it;
	it++;
	for (; it!=plan.end(); ++it) {
	   path_length += hypot(  (*it).pose.position.x - last_pose.pose.position.x, 
		                 (*it).pose.position.y - last_pose.pose.position.y );
	   last_pose = *it;
	}
	cout <<"The global path length: "<< path_length<< " meters"<<endl;
	MyExcelFile << "\t" <<path_length <<"\t"<< plan.size() <<endl;
      //publish the plan

      return true;

    }

    else
    {
      ROS_WARN("The planner failed to find a path, choose other goal position");
      return false;
    }

  }

  else
  {
    ROS_WARN("Not valid start or goal");
    return false;
  }

}
void RAstarPlannerROS::getCorrdinate(float& x, float& y)
{

  x = x - originX;
  y = y - originY;

}

int RAstarPlannerROS::convertToCellIndex(float x, float y)
{

  int cellIndex;

  float newX = x / resolution;
  float newY = y / resolution;

  cellIndex = getCellIndex(newY, newX);

  return cellIndex;
}

void RAstarPlannerROS::convertToCoordinate(int index, float& x, float& y)
{

  x = getCellColID(index) * resolution;

  y = getCellRowID(index) * resolution;

  x = x + originX;
  y = y + originY;

}

bool RAstarPlannerROS::isCellInsideMap(float x, float y)
{
  bool valid = true;

  if (x > (width * resolution) || y > (height * resolution))
    valid = false;

  return valid;
}

void RAstarPlannerROS::mapToWorld(double mx, double my, double& wx, double& wy){
   costmap_2d::Costmap2D* costmap = costmap_ros_->getCostmap();
    wx = costmap->getOriginX() + mx * resolution;
    wy = costmap->getOriginY() + my * resolution;
}

vector<int> RAstarPlannerROS::RAstarPlanner(int startCell, int goalCell){

   vector<int> bestPath;


//float g_score [mapSize][2];
float g_score [mapSize];

for (uint i=0; i<mapSize; i++)
	g_score[i]=infinity;

   timespec time1, time2;
  /* take current time here */
   clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &time1);

  bestPath=findPath(startCell, goalCell,  g_score);

   clock_gettime(CLOCK_PROCESS_CPUTIME_ID, &time2);


   cout<<"time to generate best global path by Relaxed A* = " << (diff(time1,time2).tv_sec)*1e3 + (diff(time1,time2).tv_nsec)*1e-6 << " microseconds" << endl;
   
   MyExcelFile <<"\t"<< (diff(time1,time2).tv_sec)*1e3 + (diff(time1,time2).tv_nsec)*1e-6 ;

  return bestPath;

}

vector<int> RAstarPlannerROS::findPath(int startCell, int goalCell, float g_score[])
{
	value++;
	vector<int> bestPath;
	vector<int> emptyPath;
	cells CP;

	multiset<cells> OPL;
	int currentCell;
	g_score[startCell]=0;
	CP.currentCell=startCell;
	CP.fCost=g_score[startCell]+calculateHCost(startCell,goalCell);
	OPL.insert(CP);
	currentCell=startCell;
	while (!OPL.empty()&& g_score[goalCell]==infinity) 
	{
		currentCell = OPL.begin()->currentCell;
		OPL.erase(OPL.begin());
		vector <int> neighborCells; 
		neighborCells=findFreeNeighborCell(currentCell);
		for(uint i=0; i<neighborCells.size(); i++) 
		{
			if(g_score[neighborCells[i]]==infinity)
			{
				g_score[neighborCells[i]]=g_score[currentCell]+getMoveCost(currentCell,neighborCells[i]);
				addNeighborCellToOpenList(OPL, neighborCells[i], goalCell, g_score); 
			}
		}
	}

	if(g_score[goalCell]!=infinity)  
	{
		bestPath=constructPath(startCell, goalCell, g_score);
		return   bestPath; 
	}
	else
	{
		cout << "Failure to find a path !" << endl;
		return emptyPath;
	}
}

vector<int> RAstarPlannerROS::constructPath(int startCell, int goalCell,float g_score[])
{
	vector<int> bestPath;
	vector<int> path;

	path.insert(path.begin()+bestPath.size(), goalCell);
	int currentCell=goalCell;

	while(currentCell!=startCell)
	{ 
		vector <int> neighborCells;
		neighborCells=findFreeNeighborCell(currentCell);

		vector <float> gScoresNeighbors;
		for(uint i=0; i<neighborCells.size(); i++)
			gScoresNeighbors.push_back(g_score[neighborCells[i]]);
		
		int posMinGScore=distance(gScoresNeighbors.begin(), min_element(gScoresNeighbors.begin(), gScoresNeighbors.end()));
		currentCell=neighborCells[posMinGScore];

		//insert the neighbor in the path
		path.insert(path.begin()+path.size(), currentCell);
	}
	for(uint i=0; i<path.size(); i++)
		bestPath.insert(bestPath.begin()+bestPath.size(), path[path.size()-(i+1)]);

	return bestPath;
}

void RAstarPlannerROS::addNeighborCellToOpenList(multiset<cells> & OPL, int neighborCell, int goalCell, float g_score[])
{
	cells CP;
	CP.currentCell=neighborCell; 
	CP.fCost=g_score[neighborCell]+calculateHCost(neighborCell,goalCell);
	OPL.insert(CP);
	
}
vector <int> RAstarPlannerROS::findFreeNeighborCell (int CellID){
  int rowID=getCellRowID(CellID);
  int colID=getCellColID(CellID);
  int neighborIndex;
  vector <int>  freeNeighborCells;
  for (int i=-1;i<=1;i++)
    for (int j=-1; j<=1;j++){
     if ((rowID+i>=0)&&(rowID+i<height)&&(colID+j>=0)&&(colID+j<width)&& (!(i==0 && j==0))){
	neighborIndex = getCellIndex(rowID+i,colID+j);
        if(isFree(neighborIndex) )
	    freeNeighborCells.push_back(neighborIndex);
	}
    }
    return  freeNeighborCells;
 
}

bool RAstarPlannerROS::isStartAndGoalCellsValid(int startCell,int goalCell)
{ 
 bool isvalid=true;
 bool isFreeStartCell=isFree(startCell);
 bool isFreeGoalCell=isFree(goalCell);
    if (startCell==goalCell)
    { 
    isvalid = false;
    }
   else
   {
      if (!isFreeStartCell && !isFreeGoalCell)
      {
	
        isvalid = false;
      }
      else
      {
	if (!isFreeStartCell)
	{
	  
	  isvalid = false;
	}
	else
	{
	    if(!isFreeGoalCell)
	    {
	      isvalid = false;
	    }
	    else
	    {
	      if (findFreeNeighborCell(goalCell).size()==0)
	      {
		isvalid = false;
	      }
	      else
	      {
		if(findFreeNeighborCell(startCell).size()==0)
		{
		  isvalid = false;
		}
	      }
	    }
	}
      }
  }
 return isvalid;
}
 float  GstarPlannerROS::getMoveCost(int i1, int j1, int i2, int j2){
   float moveCost=INFINIT_COST;
   if((j2==j1+1 && i2==i1+1)||(i2==i1-1 && j2==j1+1) ||(i2==i1-1 && j2==j1-1)||(j2==j1-1 && i2==i1+1)){
     moveCost = 1.4;
   }
   else{
     if ((j2==j1 && i2==i1-1)||(i2==i1 && j2==j1-1)||(i2==i1+1 && j2==j1) ||(i1==i2 && j2==j1+1)){
       
       moveCost = 1;
     }
   }
   return moveCost;
 } 
   float  GstarPlannerROS::getMoveCost(int CellID1, int CellID2){
   int i1=0,i2=0,j1=0,j2=0;
   i1=getCellRowID(CellID1);
   j1=getCellColID(CellID1);
   i2=getCellRowID(CellID2);
   j2=getCellColID(CellID2);
   return getMoveCost(i1, j1, i2, j2);
 } 

 bool  GstarPlannerROS::isFree(int i, int j){
   int CellID = getCellIndex(i, j);
 return OGM[CellID];
 } 
 bool  GstarPlannerROS::isFree(int CellID){
 return OGM[CellID];
 } 
}
;
bool operator<(cells const &c1, cells const &c2) { return c1.fCost < c2.fCost; }
