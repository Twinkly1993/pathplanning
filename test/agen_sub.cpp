#include "ros/ros.h"
#include "std_msgs/String.h"
 
/**
 * This tutorial demonstrates simple receipt of messages over the ROS system.
 */
void chatterCallback(const std_msgs::String::ConstPtr& msg)
{
  ROS_INFO("it is location: [%s]", msg->data.c_str());
}
 
int main(int argc, char **argv)
{
  /
  ros::Subscriber sub = n.subscribe("chatter", 1000, chatterCallback);

  ros::spin();
 
  return 0;
}
eturn 0;
}
