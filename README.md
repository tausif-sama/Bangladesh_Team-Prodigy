## Introduction

Badur Gaddi is a self driving car, modeled to work on the WRO FE track. The self driving AI model is built with end to end Convolutional Neural Network System system build on pytorch.

## Hardware

+ Jetson Nano 4gb(A02)
+ PiCam V2(With Fisheye Lense Add on)
+ PCA9685
+ Miscellaneous actuator components

## Software & AI

Nvidia Jetson Nano SDK was used as the core os of the car

1. [Data Collection](src/autopilot_data_collection.ipynb): This is the first stage of the car. This code is used to calibrate the car, and capture data for the dataset
2. [Training](src/autopilot_training.ipynb): The captured data is divided in 70/30 proportion in the training and validation set. A custom testing set is made to get better results. The whole data is fed on to the CNN then. And the model is prepared
3. [Testing](src/autopilot_testing.py): We test the car in the real worls after training the model.

## Tweaks

+ Putting the Jetson Nano on MAXN mode gives faster inference, and better performance on track
+ For the WRO track it's wise to not have any negative throttle value in the Dataset
+ Removing bad frames improve the models accuracy.
+ The wider the field of view the better the performance. Preferably 160-180 degrees. 
+ Using python script to run the notebook lowers the latency.
+ Bigger datasets can be too hardware demanding for the car. Saving frequently helps the car to perform better. 

