## Software & Setup

#### Prerequisites

1. SD Card(Preferably 128gb)
2. SD Card Reader
3. balenaEtcher or Rufus

#### Steps

1. Download Jetpack V4.6 from nvidia's official website
2. Burn that image into the SD card using balenaEtcher
3. Install that SD card and into jetson and turn it on
4. The setup process is pretty self explanatory. Complete it as guided
5. Open terminal and type in sudo apt update
6. After that stage is complete, type in sudo apt upgrade
7. After getting everything up to date in the os, now it’s time to install all the dependencies from the code(i.e, OpenCV)
8. Once all the installation is done, now it’s time to check and calibrate the thresholds
9. Use the cam.py file to test if the camera is working properly. If the camera is flipped 180 degrees. Then change the flip_method=2 to flip__method=0
10. Now it’s time to identify the objects. We have already included the threshold for Orange Line, Blue Line, Green Trafic Bar, Red Trafic Bar, and Black wall. But, it might differ drastically based on the lighting and color of the objects in different situations. So, we suggest checking and calibrating it with this code. 
11. Next up is servo. It’s often hard to know the servo angles correctly before testing it. The  servo.py script is for you to test the servo angles. Just change the angle variable in the code, and you will find the values you need. Ensure that you are the bus channel is correct on your code(inferred from PCA9685). Which in our case was 0.
12. The speed of the car is pivotal to this whole algorithm, throttle.py script is there to help you get the sweet spot for your speed. Put your car’s rear wheels higher than the ground at the beginning of the test to avoid collision. Once you are comfortable tinkering with the motor gpio.pwm try it on the ground.
13. It’s finally time to go headless. But SSH isn’t the best option here, as there is a lot of graphical interface required for the tuning. So we will use a VNC viewer. Download VNC viewer in your pc, and prepare the jetson as a VNC server. Once the Jetson is connected to your local network, find it’s IP from the routers admin panel. We suggest binding the ip with the device in the router for further convenience. Now just type in the ip in the VNC viewer and you are connected to the car.
14. If you made this far properly. You are now ready to run the code flawlessly. Just put the car on track and run the code in the terminal, and see the magic. 

