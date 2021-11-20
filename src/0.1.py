import cv2
import time
import numpy as np
from adafruit_servokit import ServoKit
import RPi.GPIO as GPIO
import serial
lab=0
select=0
order=0
GPIO.setwarnings(False)
GPIO.setup('LCD_BL_PW',GPIO.OUT)

def perspective(image):
    source = np.float32([(46,140),(320,140),(12,214),(350,214)])
    #Region of intrest
    image1=image.copy()
    # image1  = cv2.line(image,(46,140),(320,140), (0,0,255),2)
    # image1  = cv2.line(image,(320,140),(350,214), (0,0,255),2)
    # image1  = cv2.line(image,(350,214),(12,214), (0,0,255),2)
    # image1  = cv2.line(image,(12,213),(46,140), (0,0,255),2)
    
    destination = np.float32([(80,0),(280,0),(80,240),(280,240)])   
    # #Perspective frame
    # image  = cv2.line(image,(60,0),(300,0), (0,255,0),2)
    # image  = cv2.line(image,(300,0),(300,240), (0,255,0),2)
    # image  = cv2.line(image,(300,240),(60,240), (0,255,0),2)
    # image  = cv2.line(image,(60,240),(60,0), (0,255,0),2)
    matrix = cv2.getPerspectiveTransform(source,destination)
    imgWarp = cv2.warpPerspective(image1,matrix,(360,240))
    return image1,imgWarp

def Threshold(img,im):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    imag = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    orange_mask = cv2.inRange(hsv,(10, 100, 20), (25, 255, 255) ) 
    blue_mask   =  cv2.inRange(hsv,(74, 69, 0), (139, 255, 255) ) 
    #img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_gray=hsv[10:236,83:279]
    red=imag[0:,90:270]
    green=imag[0:,90:270]
    red=cv2.inRange(red,(146, 50, 40), (179, 255, 255) )
    green=cv2.inRange(green,(25, 75, 39), (163, 255, 255) )
    wall=cv2.inRange(img_gray,(0, 0, 0), (179, 255, 90) )
    #imgthres = cv2.inRange(hsv,lower_gray,upper_gray)
 
    return orange_mask,wall,blue_mask,red,green



def getHistogram(orangeline,wallimg,blueline,red,green,region=1): 
    OhistValues = np.sum(orangeline, axis=0)
    BhistValues = np.sum(blueline, axis=0)
    
    
    wallhistValues = np.sum(wallimg, axis=0)
    redv = np.sum(red, axis=0)
    greenv = np.sum(green, axis=0)
    redv= np.max(redv)
    greenv=np.max(greenv)

    Orange=np.max(OhistValues)
    Blue=np.max(BhistValues)
    print(Blue)
    global select
    global order
    if Orange>6000 or Blue>6000:
        if select==0:
            if Orange>Blue:
                order=1
            elif Blue>Orange:
                order=2
        
        
    print(order)
    global lab
    if order==1:
        select=1
        if lab<=12:
            print("clockwise lab:"+str(lab))
            ard = read()

            if Orange>7000 and ard[0]>50: 
                lab+=1
                motor.ChangeDutyCycle(30)
                robot.servo[0].angle=120
                time.sleep(1.9)
                print("turn")
            elif Orange>7000 and ard[0]<50:
                lab+=1 
                while ard[0]<50:
                    motor.ChangeDutyCycle(25)    
                    ard = read() 
                    print("i am in whileloop")
                #time.sleep(0.2)
                if ard[1]<20:

                    robot.servo[0].angle=120
                    motor.ChangeDutyCycle(40)
                    time.sleep(1.2)
            
                else:
                    robot.servo[0].angle=120
                    motor.ChangeDutyCycle(30)
                    time.sleep(1.6)
                print("rturn")
            else:
                motor.ChangeDutyCycle(0)
    
    if order==2:
        select=1
        if lab<=12:
            print("counterclock lab:"+str(lab))
            ard = read()

            if Blue>7000 and ard[1]>50: 
                lab+=1
                motor.ChangeDutyCycle(30)
                robot.servo[0].angle=50
                time.sleep(1.9)
            # print("leturn")
            elif Blue>7000 and ard[1]<50:
                lab+=1 
                while ard[1]<50:
                    motor.ChangeDutyCycle(35)
                        
                    ard = read() 
                    print("sidewall")
            #time.sleep(0.2)
                if ard[0]<20:

                    robot.servo[0].angle=50
                    motor.ChangeDutyCycle(40)
                    time.sleep(1.2)
            
                else:
                     robot.servo[0].angle=50
                     motor.ChangeDutyCycle(30)
                     time.sleep(1.6)
            # print("close left turn")
            else:
                motor.ChangeDutyCycle(0)

    size = len(wallhistValues)
    leftpos = np.max(wallhistValues[0:size//2])
    #print(leftpos)
    rightpos= np.max(wallhistValues[size//2:])
    #print(rightpos)
    motor.ChangeDutyCycle(30)

    if leftpos>8000 or  rightpos>8000:
        if leftpos>rightpos:
            print("Wall Left")
            robot.servo[0].angle=120
            time.sleep(0.1)
    
            
        elif rightpos>leftpos:
            print("Wall Right")
            robot.servo[0].angle=50
            time.sleep(0.1)


    if redv>6000:
        robot.servo[0].angle=120
        motor.ChangeDutyCycle(25) 
        time.sleep(0.1)
        print("red")
    if greenv>6000:
        robot.servo[0].angle=50
        motor.ChangeDutyCycle(25)
        print("Green")
        time.sleep(0.1) 
    



    
    


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
        dddd=read()
        #making copy img for sign detection
        sign = img.copy()

        #Getting width and height for detectnet
        height=img.shape[0]
        width=img.shape[1]
        robot.servo[0].angle=79
        
        #color Detection
        img1,imgwarp = perspective(img)
        orange_line,wallthre,blue_line,redb,greenb  = Threshold(imgwarp,img)
        getHistogram(orange_line,wallthre,blue_line,redb,greenb)
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
        cv2.imshow('Orange', orange_line)
        cv2.imshow('Blue', blue_line)
        cv2.imshow('Walls', wallthre)
        cv2.imshow('Final',greenb)

        # condition if space is pressed break from loop
        if lab==12:
            robot.servo[0].angle=79
            motor.ChangeDutyCycle(26)
            time.sleep(1.2)
            motor.ChangeDutyCycle(0)
            break
        k = cv2.waitKey(1)
        if k%256 == 32:
            motor.ChangeDutyCycle(0)
            robot.servo[0].angle=79
            break

