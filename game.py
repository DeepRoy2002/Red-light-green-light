import random

import cv2
import os
import numpy as np
import time
#from playsound import playsound

folderPath = 'frames'
mylist = os.listdir(folderPath)
graphic = [cv2.imread(f'{folderPath}/{imPath}') for imPath in mylist]
green = graphic[0];
red = graphic[1];
kill = graphic[2];
winner = graphic[3];
intro = graphic[4];

cv2.imshow('Squid Game', cv2.resize(intro, (0, 0), fx=0.69, fy=0.69))
cv2.waitKey(1)
while True:
    cv2.imshow('Squid Game', 
               cv2.resize(intro, (0, 0), fx=0.69, fy=0.69))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
TIMER_MAX =45
TIMER =TIMER_MAX
maxMove = 6500000
font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture(0)
frameHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frameWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)

win =False
prev=time.time()
showFrame = cv2.resize(green,(0,0),fx=0.69,fy=0.69)
isgreen=True

while cap.isOpened() and TIMER>=0:
    if isgreen and (cv2.waitKey(10) & 0xFF == ord('w')):
        win = True
        break
    ret,frame = cap.read()
    cv2.putText(showFrame,str(TIMER),(50,50),font,1,
                (0,int(255*(TIMER)/TIMER_MAX),int(255*(TIMER_MAX-TIMER)/TIMER_MAX)),4,cv2.LINE_AA)

