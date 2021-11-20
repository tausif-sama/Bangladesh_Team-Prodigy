from adafruit_servokit import ServoKit
# from adafruit_motorkit import MotorKit
import time
robot=ServoKit(channels=16)
robot.servo[0].angle=79
