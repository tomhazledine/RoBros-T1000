# Robot Motor Test Script

import RPi.GPIO as GPIO
import time

# Setup the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pinMotorAForwards = 10
pinMotorABackwards = 9
pinMotorBForwards = 7
pinMotorBBackwards = 8
pinLineFollower = 25

# Set the GPIO Pin mode
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)
GPIO.setup(pinLineFollower, GPIO.IN)

# Turn all motors off
def StopMotors():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 0)

# Turn both motors forwards
def Forwards():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)

# Turn both motors backwards
def Backwards():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 1)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 1)

# Turn left
def Left():
    GPIO.output(pinMotorAForwards, 0)
    GPIO.output(pinMotorABackwards, 1)
    GPIO.output(pinMotorBForwards, 1)
    GPIO.output(pinMotorBBackwards, 0)

# Turn Right
def Right():
    GPIO.output(pinMotorAForwards, 1)
    GPIO.output(pinMotorABackwards, 0)
    GPIO.output(pinMotorBForwards, 0)
    GPIO.output(pinMotorBBackwards, 1)

# Forwards()
# time.sleep(1)

# Left()
# time.sleep(0.5)

# Right()
# time.sleep(0.5)

# Backwards()
# time.sleep(0.5)

# StopMotors()

# Reset the GPIO pins (turns off motors too)
# GPIO.cleanup()

try:
    # Repeat:
    while True:
        print(GPIO.input(pinLineFollower))
        if GPIO.input(pinLineFollower)==0:
            StopMotors()
            print('The sensor is seeing a black surface')
        else:
            Forwards()
            print('The sensor is seeing a white surface')
        time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()