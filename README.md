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


