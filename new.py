import os#2
import cv2#3
import time#7
import random #9
import numpy as np #10

folderpath = 'frames' #1 defining the assets folder
mylist = os.listdir(folderpath) #2 lisitng the assets of the assets folder
graphics  = [cv2.imread(f'{folderpath}/{imgpath}') for imgpath in mylist]# 3 reading and storing the assets in a list
green = graphics[0]
red = graphics[1]
kill = graphics[2]
winner = graphics[3]
intro = graphics[4]

#4assigning the assets to variables
#5--------------------------------INTRO SCREEN---------------------------------------
cv2.imshow('Squid Game', cv2.resize(intro, (0, 0), fx=0.69, fy=0.69))
cv2.waitKey(1)
while True:
    cv2.imshow('Squid Game', cv2.resize(intro, (0, 0), fx=0.69, fy=0.69))
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#RUNS TILL q IS PRESSED
#------------------GAME RULES--------------------------------#6

TIMER_MAX = 30 #max time
TIMER = TIMER_MAX
maxMove = 6500000 #max feature extraction score
font = cv2.FONT_HERSHEY_SIMPLEX #text font
cap = cv2.VideoCapture(0) #webcam capturing
frameHeight = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
frameWidth = cap.get(cv2.CAP_PROP_FRAME_WIDTH)#getting the height and width of the captured vid

win = False
prev =time.time()
prevDoll = prev
showFrame = cv2.resize(green, (0, 0), fx=0.69, fy=0.69) #green light resize
isgreen = True#atfirst lets insure that only green is there
#GAME LOGIC AND WINNING CONDITIONS-------------------------#8

while cap.isOpened() and TIMER >= 0:
#if cam is opened and the timer i.e. initialized at max timer =30 >= 0
    # press 'w' to win
    if isgreen and (cv2.waitKey(10) & 0xFF == ord('w')):
        win = True
        break

    ret, frame = cap.read()#frame is reading the webcam stream

    cv2.putText(showFrame, str(TIMER),
                (50, 50), font,
                1, (0, int(255 * (TIMER) / TIMER_MAX), int(255 * (TIMER_MAX - TIMER) / TIMER_MAX)),
                4, cv2.LINE_AA)#putting the text on the window which shows the timer i.e. time decreasing,
                #also the color of the text chnages as the time passes by
    # current time
    #after doing all this some time must have passed
    cur = time.time()
    # Update and keep track of Countdown
    # if time elapsed is one second
    # than decrease the counter
    
    no = random.randint(1, 5) #generate a random number between 1 and 5
    
    if cur - prev >= no: #if more than the random time has elapsed then 
        prev = cur #give prev the current time
        TIMER = TIMER - no #timer is reduced
        if cv2.waitKey(10) & 0xFF == ord('w'):
            win = True
            break#win condition before changing colors

        if isgreen:
            showFrame = cv2.resize(red, (0, 0), fx=0.69, fy=0.69)#change colors
            isgreen = False #set aflag that will be verified later
            ref = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        else:
            showFrame = cv2.resize(green, (0, 0), fx=0.69, fy=0.69)#change colors
            isgreen = True #set a flag that will be verified later
    if not isgreen:#when red screen is there
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frameDelta = cv2.absdiff(ref, gray)
        thresh = cv2.threshold(frameDelta, 20, 255, cv2.THRESH_BINARY)[1]
        change = np.sum(thresh)
        if change > maxMove:
            break
        #motion detection when the movt causes enough change in intensity in grayscale
    else:
        if cv2.waitKey(10) & 0xFF == ord('w'):
            win = True
            break
            #when green sign condition
    
    camShow = cv2.resize(frame, (0, 0), fx=0.4, fy=0.4) #camera resize
    camH, camW = camShow.shape[0], camShow.shape[1]#getting the height and width
    showFrame[0:camH, -camW:] = camShow #setting it to the top right corner

    cv2.imshow('Squid Game', showFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

    # press 'w' to win
    if isgreen and (cv2.waitKey(10) & 0xFF == ord('w')):
        win = True
        break

#GAME END-----------------------11
cap.release()
if not win:
    for i in range(10):
        cv2.imshow('Squid Game', cv2.resize(kill, (0, 0), fx=0.69, fy=0.69))
    while True:
        cv2.imshow('Squid Game', cv2.resize(kill, (0, 0), fx=0.69, fy=0.69))
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
else:

    cv2.imshow('Squid Game', cv2.resize(winner, (0, 0), fx=0.69, fy=0.69))
    cv2.waitKey(125)

    while True:
        cv2.imshow('Squid Game', cv2.resize(winner, (0, 0), fx=0.69, fy=0.69))
        # cv2.imshow('shit',cv2.resize(graphic[3], (0, 0), fx = 0.5, fy = 0.5))
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cv2.destroyAllWindows()