import sys
from subprocess import call
import time

speed1 = int(sys.argv[1])
speed2 = int(sys.argv[2])

motor1 = 0x0a
motor2 = 0x0b

if (speed1 < 0):
    #2's compliment
    speed1 = hex(((abs(speed1) ^ 0xffff) + 1) & 0xffff)
if (speed2 < 0):
    #2's compliment
    speed2 = hex(((abs(speed2) ^ 0xffff) + 1) & 0xffff)

def i2cwrite(address, register, value):
    call(["i2cset", "-y", "1", str(address), str(register), str(value)])

def i2cwritel(address, register, value):
    call(["i2cset", "-y", "1",  str(address), str(register), str(value), "w"])

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