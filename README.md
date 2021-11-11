Engineering materials
====

This repository contains engineering materials of a self-driven vehicle's model participating in the WRO Future Engineers competition in the season 2021 from Team Bangladesh.

Badur Gaddi v0.1.50 for WRO Future Engineers.
This repository contains full documentation of our robot. 

## Content

* `team_photos` contains 2 photos of the team
* `youtube_link` contains the video of the robot 
* `robot_photos` contains 6 photos of the vehicle (from every side, from top and bottom)
* `schematics` contains schematic diagrams of the electromechanical components illustrating all the elements (electronic components and motors) used in the vehicle and how they connect to each other.
* `src` contains code of control software for all components which were programmed
* `chassis` is for the files and documentation of the chassis assembly
* `other` is for other misc files 

## Introduction

Badur Gaddi is a self driving car, modeled to work on the WRO FE track. The self driving AI model is built with end to end Convolutional Neural Network System system build on pytorch.

## Haardware

+ Jetson Nano 4gb(A02)
+ PiCam V2(With Fisheye Lense Add on)
+ PCA9685
+ Miscellaneous actuator components

## Softwaare & AI

Nvidia Jetson Nano SDK was used as the core os of the car

1. [Data Collection](src/autopilot_data_collection.ipynb): This is the first stage of the car. This code is used to calibrate the car, and capture data for the dataset
2. Training: The captured data is divided in 70/30 proportion in the training and validation set. A custom testing set is made to get better results. The whole data is fed on to the CNN then. And the model is prepared
3. Testing: We test the caar in the real worls after traaining the model.


