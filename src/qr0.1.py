import cv2
import time
import numpy as np
from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO
import serial
lab=0


GPIO.setwarnings(False)
GPIO.setup('LCD_BL_PW',GPIO.OUT)

def perspective(image):
    source = np.float32([(46,140),(320,140),(12,214),(350,214)])
    #Region of intrest
    image1=image.copy()
    image1  = cv2.line(image,(46,140),(320,140), (0,0,255),2)
    image1  = cv2.line(image,(320,140),(350,214), (0,0,255),2)
    image1  = cv2.line(image,(350,214),(12,214), (0,0,255),2)
    image1  = cv2.line(image,(12,213),(46,140), (0,0,255),2)
    
    destination = np.float32([(80,0),(280,0),(80,240),(280,240)])   
    # #Perspective frame
    # image  = cv2.line(image,(60,0),(300,0), (0,255,0),2)
    # image  = cv2.line(image,(300,0),(300,240), (0,255,0),2)
    # image  = cv2.line(image,(300,240),(60,240), (0,255,0),2)
    # image  = cv2.line(image,(60,240),(60,0), (0,255,0),2)
    matrix = cv2.getPerspectiveTransform(source,destination)
    imgWarp = cv2.warpPerspective(image1,matrix,(360,240))
    return image1,imgWarp

def Threshold(img):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv,(10, 100, 20), (25, 255, 255) )   
    #img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray=hsv[10:236,83:279]
    thres=cv2.inRange(img_gray,(0, 0, 0), (179, 255, 90) )
    #imgthres = cv2.inRange(hsv,lower_gray,upper_gray)
 
    return mask,thres



def getHistogram(img,wallimg,minPer=0.9,display= False,region=4): 
    if region ==1:
        histValues = np.sum(img, axis=0)
    else:
        histValues = np.sum(img[img.shape[0]//region:,:], axis=0)
    
    
    wallhistValues = np.sum(wallimg, axis=0)


    size = len(wallhistValues)
    leftpos = np.max(wallhistValues[0:size//2])
    #print(leftpos)
    rightpos= np.max(wallhistValues[size//2:])
    #print(rightpos)
    if leftpos>8000 or  rightpos>8000:
        if leftpos>rightpos:
            print("Wall Left")
            robot.servo[0].angle=120
            
        elif rightpos>leftpos:
            print("Wall Right")
            robot.servo[0].angle=50
            # time.sleep(0.2)
    
    maxValue=np.max(histValues)
    print(maxValue)
    global lab
    if lab<=12:
        print("lab:"+str(lab))
        ard = read()
        motor.ChangeDutyCycle(30)
        if maxValue>8000 and ard[0]>50:
            lab+=1
            robot.servo[0].angle=120
            time.sleep(1.9)
            print("turn")
        elif maxValue>8000 and ard[0]<50:
            lab+=1 
            while ard[0]<50:
                motor.ChangeDutyCycle(25)
                ard = read() 
                print("i am in whileloop")
            #time.sleep(0.2)
            robot.servo[0].angle=120
            motor.ChangeDutyCycle(50)
            time.sleep(1.2)
            print("rturn") 

    else:
        motor.ChangeDutyCycle(0)


def read():
    data = arduino.readline()
    decode=str(data[0:len(data)].decode("utf-8"))
    listv=decode.split('x')
    listf=[]
    for item in listv:
        listf.append(int(item))
    return listf






if __name__ == '__main__':

    arduino = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=10)

    #intialization for fps
    timeStamp=time.time()
    fpsFilt=0
    robot=ServoKit(channels=16)
    robot.servo[0].angle=79
    #Camera Intialization
    cap=cv2.VideoCapture("nvarguscamerasrc  ! video/x-raw(memory:NVMM), width=(int)360, height=(int)240,format=(string)NV12, framerate=(fraction)30/1 ! nvvidconv flip-method=2 ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! queue ! appsink drop=1", cv2.CAP_GSTREAMER)
    
    #font specifying for frame
    font=cv2.FONT_HERSHEY_SIMPLEX

    motor=GPIO.PWM('LCD_BL_PW',100)
    motor.start(0)
    #while loop for camera frames
    while True:
        #Getting frames from camera
        success, img = cap.read()
        #resizing frame as required
        img = cv2.resize(img,(360,240))

        #making copy img for sign detection
        sign = img.copy()

        #Getting width and height for detectnet
        height=img.shape[0]
        width=img.shape[1]
        robot.servo[0].angle=79
        
        #color Detection
        img1,imgwarp = perspective(img)
        cannyth_add,wallthre  = Threshold(imgwarp)
        getHistogram(cannyth_add,wallthre,display=True)
        # calculating fps
        dt=time.time()-timeStamp
        timeStamp=time.time()
        fps=1/dt
        fpsFilt=.9*fpsFilt + .1*fps
        #print(str(round(fps,1))+' fps')
        
        #Putting fps on frame
        cv2.putText(img1,str(round(fpsFilt,1))+' fps',(0,30),font,1,(0,0,255),2)
        
        #Displaying all operated frames
        cv2.imshow('Orignal',img1)
        cv2.imshow('CannyFinal',cannyth_add)
        cv2.imshow('Walls', wallthre)
        cv2.imshow('Final',imgwarp)

        # condition if space is pressed break from loop
        if lab==12:
            robot.servo[0].angle=79
            motor.ChangeDutyCycle(30)
            time.sleep(1.4)
            motor.ChangeDutyCycle(0)
            break
        k = cv2.waitKey(1)
        if k%256 == 32:
            motor.ChangeDutyCycle(0)
            robot.servo[0].angle=79
            break

