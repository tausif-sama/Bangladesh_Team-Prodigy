from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO
import time

# GPIO.setmode(GPIO.TEGRA_SOC)
print(GPIO.getmode())

GPIO.setup('LCD_BL_PW',GPIO.OUT)
#GPIO.setup(32,100)
motor=GPIO.PWM('LCD_BL_PW',100)
# motor.start(70)
robot=ServoKit(channels=16)
robot.servo[0].angle=79
time.sleep(5)
motor.ChangeDutyCycle(0)
