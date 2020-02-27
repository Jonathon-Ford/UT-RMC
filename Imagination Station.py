# This code is to be used for the imagination station
# This program will ask for a set of instructions to run with the options "Forward, Backward, Turn Left, Turn Right


import RPi.GPIO as GPIO #Pin setup for Entire Pi
import time

class Station:

# pin setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

#motor variables
FR = GPIO.PWM(13,50)#Front Right Motor #The value 50 is the Frequency
FL = GPIO.PWM(22,50)#Front Left Motor #The value 12 is the GPIO pin
RR = GPIO.PWM(15,50)#Rear Right Motor
RL = GPIO.PWM(18,50)#Rear Left Motor
FR.start(100)
FL.start(100)
RR.start(100)
RL.start(100)

#Define functions for kids to use

def forward(length):
    FR.ChangeDutyCycle(6.5)
    FL.ChangeDutyCycle(8)
    RR.ChangeDutyCycle(6.5)
    RL.ChangeDutyCycle(8)
    time.sleep(length)
    FR.ChangeDutyCycle(100)
    FL.ChangeDutyCycle(100)
    RR.ChangeDutyCycle(100)
    RL.ChangeDutyCycle(100)

def turn_right():
    FR.ChangeDutyCycle(10)
    FL.ChangeDutyCycle(10)
    RR.ChangeDutyCycle(10)
    RL.ChangeDutyCycle(10)
    time.sleep(.51)
    FR.ChangeDutyCycle(100)
    FL.ChangeDutyCycle(100)
    RR.ChangeDutyCycle(100)
    RL.ChangeDutyCycle(100)

def turn_left():
    FR.ChangeDutyCycle(5)
    FL.ChangeDutyCycle(5)
    RR.ChangeDutyCycle(5)
    RL.ChangeDutyCycle(5)
    time.sleep(.51)
    FR.ChangeDutyCycle(100)
    FL.ChangeDutyCycle(100)
    RR.ChangeDutyCycle(100)
    RL.ChangeDutyCycle(100)

def stop():
    FR.ChangeDutyCycle(100)
    FL.ChangeDutyCycle(100)
    RR.ChangeDutyCycle(100)
    RL.ChangeDutyCycle(100)

def reverse():
    FR.ChangeDutyCycle(8)
    FL.ChangeDutyCycle(6.5)
    RR.ChangeDutyCycle(8)
    RL.ChangeDutyCycle(6.5)

#Print instructions
print("To go forward type forward(time): where time is how long the robot runs")
print("To turn right 90 degrees type turn_right()")
print("To turn left 90 degrees type turn_left()")
print("To stop type stop(), and to abort press q")
print("Using these functions program the robot through the obstacle course!")
