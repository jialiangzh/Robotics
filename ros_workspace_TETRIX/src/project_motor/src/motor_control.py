#!/usr/bin/env python

import sys
import rospy
from subprocess import call
import time
from std_msgs.msg import String
import math

motor1 = 0x0a
motor2 = 0x0b
pub = rospy.Publisher('motor', String)

def i2cwrite(address, register, value):
    call(["i2cset", "-y", "1", str(address), str(register), str(value)])

def i2cwritel(address, register, value):
    call(["i2cset", "-y", "1",  str(address), str(register), str(value), "w"])

def listener():

    str = ''
    while not str == 's': 
        str = raw_input("please enter start:")
        
    rospy.init_node('control_listener', anonymous=True)
    rospy.Subscriber('command_velocity', String, callback, queue_size=1)
    
    while not str == 'e':
        str = raw_input("please enter end:")

#    while not rospy.is_shutdown():
#        rospy.
#    try:
#        rospy.spin()
#    except KeyboardInterrupt:
#        print("interrupted")
    rospy.signal_shutdown(None)
    motor_stop()
    print("executed")
    sys.exit()
    
def callback(message):

#    print("got here\n")
    """
    message_data = message.data
    message_split = message_data.split(", ")
    x = int(message_split[0])
    y = int(message_split[1])

    rot_speed = 0    
    delta_x = x - 340
    delta_y = y - 340
    forwardCount = 0

    if abs(delta_x) > 50:
        rot_speed = delta_x / abs(delta_x) * 17
        print("delta_x: ", delta_x)
        motor_go(rot_speed, 0-rot_speed)
        motor_stop()
    else:
       #rot_speed = int(16 * float(abs(delta_x)) / 100)
        #print(rot_speed)
        print("delta_x: ", delta_x)
        while (forwardCount < 7):
        #if y < 400:
            motor_go(100,100)
            print("forward, y: ", y)
            forwardCount+=1
        motor_stop()
        forwardCount = 0
        print("stopped:", x, y)
    #motor_go(rot_speed, 0-rot_speed)
    #pub.publish("motor_run")
    """
    [v1, v2] = message.data.split(', ')
    print('got ' + str(v1) + str(v2))
    if v1 == '101':
    	for i in range(0, 10):
            motor_go(100, 100)
        motor_stop()
    else:
        motor_go(int(v1), int(v2))
        motor_stop()

    # mid_x_min = 330
    # mid_x_max = 350

    # speed1 = 0
    # speed2 = 0
    # if x < mid_x_min:
    #     print('turn left')
    #     motor_go(-15, 15)
    # elif x > mid_x_max:
    #     print('turn right')
    #     motor_go(15, -15)
    # else:

"""

def callback(message):
    print(message.data)
"""
def motor_go(speed1, speed2):

    if (speed1 < 0):
        #2's compliment
        speed1 = hex(((abs(speed1) ^ 0xffff) + 1) & 0xffff)

    if (speed2 < 0):
        #2's compliment
        speed2 = hex(((abs(speed2) ^ 0xffff) + 1) & 0xffff)
    
    #Setup motor controller mode
    i2cwrite(motor1, 0x01, 0x13)
    i2cwrite(motor2, 0x01, 0x13)
    
    #set speed
    i2cwritel(motor1, 0x04, 0x0000) #fractional speeds aren't very interesting
    i2cwritel(motor1, 0x06, speed1)
    i2cwritel(motor2, 0x04, 0x0000)
    i2cwritel(motor2, 0x06, speed2)
    
    #set max acceleration - this should prolly not be 0x0fff.. find out what it should be
    i2cwritel(motor1, 0x90, 0x0004)
    i2cwritel(motor2, 0x90, 0x0004)
    
    #set timeout
    i2cwritel(motor1, 0x80, 0xffff)
    i2cwritel(motor2, 0x80, 0xffff)
    
    #go!
    i2cwrite(motor1, 0x08, 0x00)
    i2cwrite(motor2, 0x08, 0x00)
    
    
    #STOP THE MOTORS
    #time.sleep(1.0)


def motor_stop():
    #Setup motor controller mode
    i2cwrite(motor1, 0x01, 0x13)
    i2cwrite(motor2, 0x01, 0x13)
    
    #set speed
    i2cwritel(motor1, 0x04, 0x0000) #fractional speeds aren't very interesting
    i2cwritel(motor1, 0x06, 0x0000)
    i2cwritel(motor2, 0x04, 0x0000)
    i2cwritel(motor2, 0x06, 0x0000)
    
    #set max acceleration - this should prolly not be 0x0fff.. find out what it should be
    i2cwritel(motor1, 0x90, 0x0004)
    i2cwritel(motor2, 0x90, 0x0004)
    
    #set timeout
    i2cwritel(motor1, 0x80, 0xffff)
    i2cwritel(motor2, 0x80, 0xffff)
    
    #go!
    i2cwrite(motor1, 0x08, 0x00)
    i2cwrite(motor2, 0x08, 0x00)

if __name__ == '__main__':
    listener()
