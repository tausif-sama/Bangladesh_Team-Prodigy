Electrical Components
====

Badur Gaddi is a self driving car, modeled to work on the WRO FE track. The self driving AI model is built with end to end Convolutional Neural Network System system build on pytorch. The electrical parts, componenets and schematic diagrams are as follows.

## Parts List

+ Jetson Nano 4gb
+ PiCam V2 
+ PCA9685 PWM Extension
+ 12V DC Geared Motor
+ MG996R Servo Motor
+ L298N Motor Driver
+ HC-SR04 Sonar Sensors
+ Arduino Nano
+ XL4015 Buck Converter
+ XL4016 Buck Converter
+ 3S LiPo battery output through XT60 Connector

## Electrical systems design decisions

- We're using the Jetson 4GB version as it has more RAM.
- PiCam V2 talks really good with the Jetson and was effortlessly connected to the CSI Camera port on the Jetson. The Camera is mounted on a articulating 3D Printed Mount.
- We're using a 12V 300RPM geared motor that provides ample Torque and Speed to drive our car weiging about 1100gm.
- The front Axel is being articulated by a MG996R Metal Gear servo.
- We've used a L298N Motor driver replacing a brushed ESC from our previous design because of the unavailability of good programmable brushed ESCs here in our country. We're only making use of the Enable pin and varying the duty cycle to control the speed as moving backwards while running in the track is not really necessary. We've set IN1 to LOW and IN2 to HIGH and we're providing a PWM on the ENA from Jetson Pin 32.
- We're using 2x HC-SR04 sonar sensors to measure distance from both the left and right walls.
- The distance data is received by the Arduino Nano and then the data is sent over to the Jetson nano through the usb port.
- 2 Buck converters were used because providing sustained voltage to the motor driver is an absolute necessity for achieving consistent performance. XL4015 Provides a constant 8.5v to the Motor driver. While the XL4016 provides clean 20W of power (5V 4A) to the Jetson.
- A 3S 12.6V 1100mAh battery is powering this entire system. We're getting a runtime of average 40min.

## Steps to replicate the exact same electrical design

100. First list item
     - First nested list item
       - Second nested list item
100. First list item
     - First nested list item
       - Second nested list item
100. First list item
     - First nested list item
       - Second nested list item
100. First list item
     - First nested list item
       - Second nested list item
100. First list item
     - First nested list item
       - Second nested list item
100. First list item
     - First nested list item
       - Second nested list item
100. First list item
     - First nested list item
       - Second nested list item


