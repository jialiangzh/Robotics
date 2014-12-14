#!/usr/bin/env python

import sys
import rospy
import time
from std_msgs.msg import String

def talker():
  #Run this program as a new node in the ROS computation graph 
  #called /talker.
  rospy.init_node('my_talker', anonymous=True)

  #Create an instance of the rospy.Publisher object which we can 
  #use to publish messages to a topic. This publisher publishes 
  #messages of type std_msgs/String to the topic /chatter_talk
  pub = rospy.Publisher('trajectory', String)
  
  # Create a timer object that will sleep long enough to result in
  # a 10Hz publishing rate
  r = rospy.Rate(10) # 10hz

  # Loop until the node is killed with Ctrl-C
  while not rospy.is_shutdown():
    # Construct a string that we want to publish
    pub_string = "150, 200"
#    pub_time = rospy.get_time()
    
    # Publish our string to the 'chatter_talk' topic
    pub.publish(pub_string)
    
    # Use our rate object to sleep until it is time to publish again
    r.sleep()
      
# This is Python's sytax for a main() method, which is run by default
# when exectued in the shell
if __name__ == '__main__':
  # Check if the node has received a signal to shut down
  # If not, run the talker method
  try:
    talker()
  except rospy.ROSInterruptException: pass