import numpy as np
import cv2
capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 320)
capture.set(cv2.CAP_PROP_FPS, 90)

backsub = cv2.bgsegm.createBackgroundSubtractorMOG() #background subtraction to isolate moving cars


counter = 0
val = 0
x = 0
y = 0
sen = 0
obs = 0
minArea=1
lineCount = 50
linePoint = 350

if capture.isOpened():
    ret, frame = capture.read()
else:
    ret = False

while ret:
    ret, frame = capture.read()
    if ret==False:
        break
    
    fgmask = backsub.apply(frame, None, 0.01)
    erode=cv2.erode(fgmask,None,iterations=3)     #erosion to erase unwanted small contours
    moments=cv2.moments(erode,True)               #moments method applied
    area=moments['m00']
    
    if moments['m00'] >=minArea:
        x=int(moments['m10']/moments['m00'])
        y=int (moments['m01']/moments['m00'])
        if x<lineCount:
            sen=sen<<1
        else:
            sen=(sen<<1)|1
        sen=sen&0x03
        if sen==1:
            counter=counter+1
        
        cv2.circle(frame,(x,y),5,(0,0,255),-1) #center, radius, colour, -1=fill


    cv2.line(frame,(lineCount,0),(lineCount,320),(0,255,0),2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'counter='+str(counter), (10,30),font,1, (255, 0, 0), 2)
    
    
    
    if moments['m00'] >=minArea:
        x=int(moments['m10']/moments['m00'])
        y=int (moments['m01']/moments['m00'])
        if x<linePoint:
            obs=obs<<1
        else:
            obs=(obs<<1)|1
        obs=obs&0x03
        if obs==1:
            val=val+1
        
        cv2.circle(frame,(x,y),5,(0,0,255),-1) #center, radius, colour, -1=fill


    cv2.line(frame,(linePoint,0),(linePoint,320),(0,255,0),2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame,'val='+str(val), (200,30),font,1, (255, 0, 0), 2)
    origin = counter - val
    if origin >=3:
        cv2.putText(frame,'sig= +10sec', (200,90),font,1, (255, 0, 0), 2)
    else:
        cv2.putText(frame,'sig= def', (200,90),font,1,(255, 0, 0), 2)
    #cv2.putText(frame,'x='+str(x)+' y='+str(y), (10,60),font,1, (255, 0, 0), 2)
    
    cv2.imshow("counter", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break