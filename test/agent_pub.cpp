#include "ros/ros.h"
#include "std_msgs/String.h"
#include<geometry_msgs/Twist.h> 

using namespace std;

#define ox 2
#define oy 5
#define pi 3.1415926

int main(int argc, char *argv[])
{
    ros::init(argc, argv, "vel_ctrl");  
    ros::NodeHandle n;               
    ros::Publisher vel_pub = n.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 10);
    ros::Publisher chatter_pub = n.advertise<std_msgs::String>("chatter", 1000);
    ros::Rate loop_rate(10);
    while(ros::ok())
    {
        geometry_msgs::Twist vel_cmd;
        out_ctrl.linear.x=2.0;
        out_ctrl.linear.y=0.0;
        out_ctrl.linear.z=0.0;
        ros::spinOnce();
        err_x=ox-x;
        err_y=oy-y;
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

    if(err_theta<-0.05 && err_theta>-pi)  out_ctrl.angular.z=pi;
    else if(err_theta>0.05 && err_theta<pi)  out_ctrl.angular.z=-pi;
    else out_ctrl.angular.z=0;
  
    if(abs(err_dis)>0.01 && out_ctrl.angular.z==0)out_ctrl.linear.x=5;
    else out_ctrl.linear.x=0.0;
  
    ROS_INFO("\nThe out_ctrl.linear.x:\n\t%f\nThe out_ctrl.angular.z:\n\t%f",out_ctrl.linear.x,out_ctrl.angular.z);
    pub.publish(out_ctrl);

    irate=0;
    }
    return 0;
}