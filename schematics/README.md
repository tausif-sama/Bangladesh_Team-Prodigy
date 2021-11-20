Electrical Systems Design
====

Badur Gaddi is a self driving car, modeled to work on the WRO FE track. The electrical parts, componenets and schematic diagrams are as follows.

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

## Design decisions

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

+  Replicating the Power system
    - Connect the main power from the XT60 connector to the both buck converters. XL4015 and XL4016. Set the output voltages to 9v (Whatever voltage your motor needs) and 5V respectively. (You'll need to split the power input from a single XT60 to 2 output sources)
    - Connect the Output of the XL4015 to the 12v and GND Pins of the L298N.
    - Connect the output of the XL4016 to a barrel connector and connect it to the input of the Jetson Nano. Double check polarity and voltage as Jetson can tolerate 4.75V to 5.25V
    - We're going to use the built in voltage regulator of the L298N to power our servo. Connect the GND and 5V wires to the power input of the PCA9685.
    - Connect motor wires to Out 1. And connect the Arduino nano to the USB port of the Jetson Nano using a mini usb cable.
+  Connecting all the logic wires
    - Connect PiCam V2 through the CSI Camera port.
    - Follow the Schematics for detailed wiring guidelines.
    - Connect the SCL, SDA, VCC and GND from the PCA9685 to the 5, 3, 1, 6 on the Jetson respectively. Connect ENA from L298N to Pin 32 on the Jetson.
    - Connect the Sonar 1 Echo, Trig and Sonar 2 Echo, Trig pins to the 2, 3 and 5, 6 pins on the Arduino Nano and power them through the 5V and GND of the Nano.
    - The IN1 pin on the L298N is connected to GND to provide a low signal and IN2 is connected to 5V to provide a HIGH signal so that the motor rotates forward. We're only making use of the Enable pin to control speed varying the duty cycle. (Follow datasheet for more info on this)
    - Connect the servo to the PCA9685 to any of the channels as it can later be changed in the code.
    
      



