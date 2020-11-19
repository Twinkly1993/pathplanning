#include "ros/ros.h"
#include "std_msgs/String.h"
#include<geometry_msgs/Twist.h>
#include<turtlesim/Pose.h>
#include<turtlesim/Color.h>
#include<math.h>

using namespace std;

#define ox 7
#define oy 7
#define pi 3.1415926

int Inpointx=0,Inpointy=0;
ros::Publisher pub;
void Callback(const turtlesim::Pose& pose)
{
  float x,y,theta,lv,av;
  float err_x,err_y,err_theta,err_dis;
  geometry_msgs::Twist out_ctrl;
  turtlesim::Pose hope_pose;
	//初始化
  out_ctrl.linear.x=1.0;
  out_ctrl.linear.y=0.0;
  out_ctrl.linear.z=0.0;
  out_ctrl.angular.x=0.0;
  out_ctrl.angular.y=0.0;
  out_ctrl.angular.z=0.0;
  x	=  pose.x;
  y	=  pose.y;
  theta	=  pose.theta;
  if(theta<0)theta=2*pi+theta;
  lv	=  pose.linear_velocity;
  av	=  pose.angular_velocity;
  ROS_INFO("\nThe pose:\n\tx:%f \n\ty:%f \n\ttheta:%f \n\tlv:%f \n\tav:%f",x,y,theta,lv,av);
	//计算
  err_x=Inpointx-x;
  err_y=Inpointy-y;
  err_dis=err_x*err_x+err_y*err_y;

  if	 (err_x==0&&err_y==0)  hope_pose.theta=0;
  else if(err_x>0&&err_y==0)  hope_pose.theta=0;
  else if(err_x>0&&err_y>0)  hope_pose.theta=atan(err_y/err_x);
  else if(err_x==0&&err_y>0)  hope_pose.theta=pi/2;
  else if(err_x<0&&err_y>0)  hope_pose.theta=atan(err_y/err_x)+pi;
  else if(err_x<0&&err_y==0)  hope_pose.theta=pi;
  else if(err_x<0&&err_y<0)  hope_pose.theta=atan(err_y/err_x)+pi;
  else if(err_x==0&&err_y<0)  hope_pose.theta=pi/2+pi;
  else if(err_x>0&&err_y<0)  hope_pose.theta=atan(err_y/err_x)+2*pi;

  err_theta=theta-hope_pose.theta;
  if(err_theta>pi){
    err_theta=-(2*pi-err_theta);
  }
  else if(err_theta<-pi){
    err_theta=2*pi+err_theta;
  }
	//附值
  if(err_theta<-0.05 && err_theta>-pi)  out_ctrl.angular.z=pi;
  else if(err_theta>0.05 && err_theta<pi)  out_ctrl.angular.z=-pi;
  else out_ctrl.angular.z=0;
  
  if(abs(err_dis)>0.01 && out_ctrl.angular.z==0)out_ctrl.linear.x=5;
  else out_ctrl.linear.x=0.0;
  
  ROS_INFO("\nThe out_ctrl.linear.x:\n\t%f\nThe out_ctrl.angular.z:\n\t%f",out_ctrl.linear.x,out_ctrl.angular.z);
  pub.publish(out_ctrl);
}

int main(int argc, char **argv)
{
  ros::init(argc, argv, "turtlectrl");
  ros::NodeHandle n1;
  cout<<"依次输入目标点的x和y坐标："<<endl;
  cin>>Inpointx>>Inpointy;
  ros::Subscriber sub = n1.subscribe("turtle1/pose", 1000, Callback);

  pub = n1.advertise<geometry_msgs::Twist>("turtle1/cmd_vel", 1000);
  ros::spin();

  return 0;
}
