#!/usr/bin/env python
import rospy
from std_msgs.msg import String

pub = rospy.Publisher('command_velocity', String)
signstored = 1

def listener():
    rospy.init_node('commander')
    rospy.Subscriber("/trajectory", String, talker, queue_size=1)
    rospy.spin()

def talker(traj):
    global signstored
    if traj.data == 'find!':
        rotation(signstored * 18)
        return
    print(traj.data)
    t = traj.data
    [x_str, y_str] = t.split(', ')
    x = int(x_str)
    y = int(y_str)
    delta_x = x - 340
    if abs(delta_x) > 50:
        speed = delta_x / abs(delta_x) * 17
        signstored = delta_x / abs(delta_x)
        rotation(speed)
        return
    if x > 450:
        rotation(20)
        signstored = 1
        return
    if x < 230:
        rotation(-20)
        signstored = -1
        return
    if y > 350:
        linear(101)
        return
    linear(100)

def linear(speed):
    print('linear, ' + str(speed))
    pub.publish(str(speed) + ', ' + str(speed))

def rotation(speed):
    print('rotation, ' + str(speed))
    pub.publish(str(speed) + ', ' + str(0-speed))

if __name__ == '__main__':
  listener()
