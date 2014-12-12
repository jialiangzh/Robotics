#!/usr/bin/env python

import sys
import rospy
from subprocess import call
import time
from std_msgs.msg import String

motor1 = 0x0a
motor2 = 0x0b

def i2cwrite(address, register, value):
    call(["i2cset", "-y", "1", str(address), str(register), str(value)])

def i2cwritel(address, register, value):
    call(["i2cset", "-y", "1",  str(address), str(register), str(value), "w"])

def listener():

    rospy.init_node('control_listener', anonymous=True)
    rospy.Subscriber('trajectory', String, callback)
    print("entered listener")
    rospy.spin()
    
def callback(message):

    print("got here\n")
    message_data = message.data
    message_split = message_data.split(", ")
    x = int(message_split[0])
    y = int(message_split[1])
    
    mid_x_min = 330
    mid_x_max = 350

    speed1 = 0
    speed2 = 0
    if x < mid_x_min:
        print('turn left')
        motor_go(-30, 30)
    elif x > mid_x_max:
        print('turn right')
        motor_go(30, -30)
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
    time.sleep(1.0)
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