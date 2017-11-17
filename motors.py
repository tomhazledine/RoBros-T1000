# Robot Motor Test Script

import RPi.GPIO as GPIO
import time

# Setup the GPIO modes
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set variables for the GPIO motor pins
pinMotorAForwards = 9
pinMotorABackwards = 10
pinMotorBForwards = 8
pinMotorBBackwards = 7
pinLineFollower = 25

# How many times to turn the pin on and off each second
Frequency = 100
# How long the pin stays on each cycle, as a percent (here, it's 30%)
DutyCycleA = 25
DutyCycleB = 25
DutyCycleA_slow = 10
DutyCycleB_slow = 10
# Setting the duty cycle to 0 means the motors will not turn
Stop = 0

# Set the GPIO Pin mode
GPIO.setup(pinMotorBForwards, GPIO.OUT)
GPIO.setup(pinMotorBBackwards, GPIO.OUT)
GPIO.setup(pinMotorAForwards, GPIO.OUT)
GPIO.setup(pinMotorABackwards, GPIO.OUT)

GPIO.setup(pinLineFollower, GPIO.IN)

# Set the GPIO to software PWM at 'Frequency' Hertz
pwmMotorAForwards = GPIO.PWM(pinMotorAForwards, Frequency)
pwmMotorABackwards = GPIO.PWM(pinMotorABackwards, Frequency)
pwmMotorBForwards = GPIO.PWM(pinMotorBForwards, Frequency)
pwmMotorBBackwards = GPIO.PWM(pinMotorBBackwards, Frequency)

# Start the software PWM with a duty cycle of 0 (i.e. not moving)
pwmMotorAForwards.start(Stop)
pwmMotorABackwards.start(Stop)
pwmMotorBForwards.start(Stop)
pwmMotorBBackwards.start(Stop)

# Turn all motors off
def StopMotors():
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Turn both motors forwards
def Forwards():
    # GPIO.output(pinMotorAForwards, 1)
    # GPIO.output(pinMotorABackwards, 0)
    # GPIO.output(pinMotorBForwards, 1)
    # GPIO.output(pinMotorBBackwards, 0)
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Turn both motors backwards
def Backwards():
    # GPIO.output(pinMotorAForwards, 0)
    # GPIO.output(pinMotorABackwards, 1)
    # GPIO.output(pinMotorBForwards, 0)
    # GPIO.output(pinMotorBBackwards, 1)
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB)

# Turn left
def Left():
    # GPIO.output(pinMotorAForwards, 0)
    # GPIO.output(pinMotorABackwards, 1)
    # GPIO.output(pinMotorBForwards, 1)
    # GPIO.output(pinMotorBBackwards, 0)
    pwmMotorAForwards.ChangeDutyCycle(Stop)
    pwmMotorABackwards.ChangeDutyCycle(DutyCycleA * 0.5)
    pwmMotorBForwards.ChangeDutyCycle(DutyCycleB * 0.5)
    pwmMotorBBackwards.ChangeDutyCycle(Stop)

# Turn Right
def Right():
    # GPIO.output(pinMotorAForwards, 1)
    # GPIO.output(pinMotorABackwards, 0)
    # GPIO.output(pinMotorBForwards, 0)
    # GPIO.output(pinMotorBBackwards, 1)
    pwmMotorAForwards.ChangeDutyCycle(DutyCycleA * 0.5)
    pwmMotorABackwards.ChangeDutyCycle(Stop)
    pwmMotorBForwards.ChangeDutyCycle(Stop)
    pwmMotorBBackwards.ChangeDutyCycle(DutyCycleB * 0.5)



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
        # print(GPIO.input(pinLineFollower))
        if GPIO.input(pinLineFollower)==0:
            # StopMotors()
            Left()
            print('\r Scanning...')
        else:
            # StopMotors()
            Forwards()
        time.sleep(0.2)

except KeyboardInterrupt:
    GPIO.cleanup()