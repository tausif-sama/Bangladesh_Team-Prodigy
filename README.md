# Engineering Documentation

## Introduction

We present you, Badur Gaddi v0.1.5. Badur Gaddi is a self driving car, modeled to work on the WRO FE track. The self driving car model is built using OpenCV and analogue sensors and given enough functionality so that it can complete a few laps at the WRO Future Engineers Track.

![maingaming](https://github.com/tausif-sama/Bangladesh_Team-Prodigy/blob/main/others/gaming.jpg)


## Content

* `chassis` contains details about our chassis and links to the 3D Printed models that we've made.
* `others` contains some miscellaneous photos.
* `robot_photos` contains the photos of our robot from all 6 sides.
* `schematics` contains detailed schematics, guidelines and instructions to replicate the same electrical system.
* `src` contains code of control software for all components which were programmed to participate in the competition.
* `team_photos` contains our photos.
* `youtube_link` contains the link to the youtube videos that show our robot in action.

Here're some photos of our robot.
![side](https://github.com/tausif-sama/Bangladesh_Team-Prodigy/blob/main/others/gaming1.jpg)
![side2](https://github.com/tausif-sama/Bangladesh_Team-Prodigy/blob/main/others/gaming2.jpg)
![baack](https://github.com/tausif-sama/Bangladesh_Team-Prodigy/blob/main/others/pasa.jpg)


## Hardware Design decisions

- We're using the Jetson 4GB version as it has more RAM.
- PiCam V2 talks really good with the Jetson and was effortlessly connected to the CSI Camera port on the Jetson. The Camera is mounted on a articulating 3D Printed Mount.
- We're using a 12V 300RPM geared motor that provides ample Torque and Speed to drive our car weiging about 1100gm.
- The front Axel is being articulated by a MG996R Metal Gear servo.
- We've used a L298N Motor driver replacing a brushed ESC from our previous design because of the unavailability of good programmable brushed ESCs here in our country. We're only making use of the Enable pin and varying the duty cycle to control the speed as moving backwards while running in the track is not really necessary. We've set IN1 to LOW and IN2 to HIGH and we're providing a PWM on the ENA from Jetson Pin 32.
- We're using 2x HC-SR04 sonar sensors to measure distance from both the left and right walls.
- The distance data is received by the Arduino Nano and then the data is sent over to the Jetson nano through the usb port.
- 2 Buck converters were used because providing sustained voltage to the motor driver is an absolute necessity for achieving consistent performance. XL4015 Provides a constant 8.5v to the Motor driver. While the XL4016 provides clean 20W of power (5V 4A) to the Jetson.
- A 3S 12.6V 1100mAh battery is powering this entire system. We're getting a runtime of average 40min.

## Steps to replicate the exact same hardware

+  Replicating the Power system
    - Connect the main power from the XT60 connector to the both buck converters. XL4015 and XL4016. Set the output voltages to 9v (Whatever voltage your motor needs) and 5V respectively. (You'll need to split the power input from a single XT60 to 2 output sources)
    - Connect the Output of the XL4015 to the 12v and GND Pins of the L298N.
    - Connect the output of the XL4016 to a barrel connector and connect it to the input of the Jetson Nano. Double check polarity and voltage as Jetson can tolerate 4.75V to 5.25V
    - We're going to use the built in voltage regulator of the L298N to power our servo. Connect the GND and 5V wires to the power input of the PCA9685.
    - Connect motor wires to Out 1. And connect the Arduino nano to the USB port of the Jetson Nano using a mini usb cable.
+  Connecting all the logic wires
    - Connect PiCam V2 through the CSI Camera port.
    - Follow the Schematics for detailed wiring guidelines.
    - Connect the SCL, SDA, VCC and GND from the PCA9685 to the 5, 3, 1, 6 on the Jetson respectively. Connect ENA from L298N to Pin 32 on the Jetson. Put a common ground connection between the jetson and L298N.
    - Connect the Sonar 1 Echo, Trig and Sonar 2 Echo, Trig pins to the 2, 3 and 5, 6 pins on the Arduino Nano and power them through the 5V and GND of the Nano.
    - The IN1 pin on the L298N is connected to GND to provide a low signal and IN2 is connected to 5V to provide a HIGH signal so that the motor rotates forward. We're only making use of the Enable pin to control speed varying the duty cycle. (Follow datasheet for more info on this)
    - Connect the servo to the PCA9685 to any of the channels as it can later be changed in the code.


## Software & Setup

#### Prerequisites

1. SD Card(Preferably 128gb)
2. SD Card Reader
3. balenaEtcher or Rufus

#### Steps

1. Download Jetpack V4.6 from nvidia's official website
 ![nvidia soft download](https://github.com/tausif-sama/Bangladesh_Team-Prodigy/blob/main/others/1.PNG)
2. Burn that image into the SD card using balenaEtcher
 ![burning iso](https://github.com/tausif-sama/Bangladesh_Team-Prodigy/blob/main/others/2a.PNG)
3. Install that SD card and into jetson and turn it on
4. The setup process is pretty self explanatory. Complete it as guided
5. Open terminal and type in sudo apt update
6. After that stage is complete, type in sudo apt upgrade
7. After getting everything up to date in the os, now it’s time to install all the dependencies from the code(i.e, OpenCV. Arduino IDE)
8. Once all the installation is done, now it’s time to check and calibrate the thresholds
9. Use the cam.py file to test if the camera is working properly. If the camera is flipped 180 degrees. Then change the flip_method=2 to flip__method=0

![camera fix](https://github.com/tausif-sama/Bangladesh_Team-Prodigy/blob/main/others/9.PNG)

10. Now it’s time to identify the objects. We have already included the threshold for Orange Line, Blue Line, Green Trafic Bar, Red Trafic Bar, and Black wall. But, it might differ drastically based on the lighting and color of the objects in different situations. So, we suggest checking and calibrating it with [hsv.py].
 
[hsv.py]: https://github.com/tausif-sama/Bangladesh_Team-Prodigy/blob/main/src/hsv.py

11. Next up is servo. It’s often hard to know the servo angles correctly before testing it. The  [servo.py] script is for you to test the servo angles. Just change the angle variable in the code, and you will find the values you need. Ensure that you are the bus channel is correct on your code(inferred from PCA9685). Which in our case was 0.
![servo angles](https://github.com/tausif-sama/Bangladesh_Team-Prodigy/blob/main/others/11.PNG)

[servo.py]: https://github.com/tausif-sama/Bangladesh_Team-Prodigy/blob/main/src/servo.py

12. The speed of the car is pivotal to this whole algorithm, [throttle.py] script is there to help you get the sweet spot for your speed. Put your car’s rear wheels higher than the ground at the beginning of the test to avoid collision. Once you are comfortable tinkering with the motor gpio.pwm try it on the ground.
![throttle](https://github.com/tausif-sama/Bangladesh_Team-Prodigy/blob/main/others/12.PNG)

[throttle.py]: https://github.com/tausif-sama/Bangladesh_Team-Prodigy/blob/main/src/throttle.py

13. It’s finally time to go headless. But SSH isn’t the best option here, as there is a lot of graphical interface required for the tuning. So we will use a VNC viewer. Download VNC viewer in your pc, and prepare the jetson as a VNC server. Once the Jetson is connected to your local network, find it’s IP from the routers admin panel. We suggest binding the ip with the device in the router for further convenience. Now just type in the ip in the VNC viewer and you are connected to the car.
![meow](https://github.com/tausif-sama/Bangladesh_Team-Prodigy/blob/main/others/13aa.PNG)
![meow](https://github.com/tausif-sama/Bangladesh_Team-Prodigy/blob/main/others/13c.PNG)
![meow](https://github.com/tausif-sama/Bangladesh_Team-Prodigy/blob/main/others/13d.PNG)
![meowe](https://github.com/tausif-sama/Bangladesh_Team-Prodigy/blob/main/others/13e.PNG)
14. If you made this far properly. You are now ready to run [main.py] flawlessly. Just put the car on track and run the code in the terminal, and see the magic. 

[main.py]: https://github.com/tausif-sama/Bangladesh_Team-Prodigy/blob/main/src/main.py

