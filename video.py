#Name: Ethan Tabachneck, Saad Ismail, Ismail Ajaz, Khalid Muhammad
#Date: 25 September 2021
#Purpose: Learn OpenCV
#Resources: https://www.mygreatlearning.com/blog/opencv-tutorial-in-python/#sh7
#What needs to happen: This only works for images at the distance that they are
#input at. To have a final product it would need to have a way to identify these
#objects at different scales. My thought which is mostly commented out is to do
#it at different scales. this ran into some issues when tring to figure out
#image sizes later on. this size shit can lead to determining the distance
#away. Also needs to determine rotation compared to the camera. if it is not
#working, adjust the threshold since that is the cutoff on the AI's certainty
#that the thing being looked at is what is being looked for. Also maybe change
#the image from the Launchpad
import numpy as np
import cv2

cap = cv2.VideoCapture(2)
img = cv2.imread('data/Launchpad.png', 0)
#img7 = cv2.resize(img, (700, 700),
#    interpolation = cv2.INTER_NEAREST)
#img6 = cv2.resize(img, (600, 600),
#    interpolation = cv2.INTER_NEAREST)
#img5 = cv2.resize(img, (500, 500),
#    interpolation = cv2.INTER_NEAREST)
#img4 = cv2.resize(img, (400, 400),
#    interpolation = cv2.INTER_NEAREST)
#img3 = cv2.resize(img, (300, 300),
#    interpolation = cv2.INTER_NEAREST)
img2 = cv2.resize(img, (200, 200),
    interpolation = cv2.INTER_NEAREST)
img1 = cv2.resize(img, (100, 100),
    interpolation = cv2.INTER_NEAREST)
#img_5 = cv2.resize(img, (50, 50),
#    interpolation = cv2.INTER_NEAREST)
w, h = img.shape[::-1]
threshold = 0.62
#lowersize = 0.1
#uppersize = 2.5
#step = 0.1
#steps = int((uppersize-lowersize)/step)

#cv2.imshow('reference', img)

#Find the center of the screen
ret, frame = cap.read()
W, H, S = frame.shape[::-1]
centW = W/2
centH = H/2

#Didn't work
#Interval between commands
#i = 0
#iup= 50


while(True):
    #Capture frame-by-frame
    ret, frame = cap.read()

    #Increment instruction counter
    #i += 1
    
    #Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #op = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            #cv2.THRESH_BINARY,11,2)
    #for x in range(0, steps):
    #    scale = lowersize+(x*step)
    #    simg = cv2.resize(fimg, (int(w*scale), int(h*scale)),
    #            interpolation = cv2.INTER_NEAREST)
#    res = cv2.matchTemplate(gray,img,eval('cv2.TM_CCOEFF_NORMED'))
#    loc = np.where(res >= threshold)
#    for pt in zip(*loc[::-1]):
#        cv2.rectangle(frame, pt, (pt[0]+w, pt[1]+h), (255,0,0), 1)
#    res7 = cv2.matchTemplate(gray,img7,eval('cv2.TM_CCOEFF_NORMED'))
#    loc7 = np.where(res7 >= threshold)
#    for pt in zip(*loc7[::-1]):
#        cv2.rectangle(frame, pt, (pt[0]+700, pt[1]+700), (255,0,0), 1)
#    res6 = cv2.matchTemplate(gray,img6,eval('cv2.TM_CCOEFF_NORMED'))
#    loc6 = np.where(res6 >= threshold)
#    for pt in zip(*loc6[::-1]):
#        cv2.rectangle(frame, pt, (pt[0]+600, pt[1]+600), (255,0,0), 1)
#    res5 = cv2.matchTemplate(gray,img5,eval('cv2.TM_CCOEFF_NORMED'))
#    loc5 = np.where(res5 >= threshold)
#    for pt in zip(*loc5[::-1]):
#        cv2.rectangle(frame, pt, (pt[0]+500, pt[1]+500), (255,0,0), 1)
#    res4 = cv2.matchTemplate(gray,img4,eval('cv2.TM_CCOEFF_NORMED'))
#    loc4 = np.where(res4 >= threshold)
#    for pt in zip(*loc4[::-1]):
#        cv2.rectangle(frame, pt, (pt[0]+400, pt[1]+400), (255,0,0), 1)
#    res3 = cv2.matchTemplate(gray,img3,eval('cv2.TM_CCOEFF_NORMED'))
#    loc3 = np.where(res3 >= threshold)
#    for pt in zip(*loc3[::-1]):
#        cv2.rectangle(frame, pt, (pt[0]+300, pt[1]+300), (255,0,0), 1)
    res2 = cv2.matchTemplate(gray,img2,eval('cv2.TM_CCOEFF_NORMED'))
    loc2 = np.where(res2 >= threshold)
    for pt in zip(*loc2[::-1]):
        cv2.rectangle(frame, pt, (pt[0]+200, pt[1]+200), (255,0,0), 1)
        #if (i >= iup):
        #    if (pt[0] > centW):
        #        print("Horizontal: Move Left")
        #    elif (pt[0] < centW):
        #        print("Horizontal: Move Right")
        #    elif (pt[0] == centW):
        #        print("Horizontal: Centered")
        #    if (pt[1] > centH):
        #        print("Vertical: Move Down")
        #    elif (pt[1] < centH):
        #        print("Vertical: Move Up")
        #    elif (pt[1] == centH):
        #        print("Vertical: Centered")
    res1 = cv2.matchTemplate(gray,img1,eval('cv2.TM_CCOEFF_NORMED'))
    loc1 = np.where(res1 >= threshold)
    for pt in zip(*loc1[::-1]):
        cv2.rectangle(frame, pt, (pt[0]+100, pt[1]+100), (255,0,0), 1)
        #if (i >= iup):
        #    if (pt[0] > centW):
        #        print("Horizontal: Move Left")
        #    elif (pt[0] < centW):
        #        print("Horizontal: Move Right")
        #    elif (pt[0] == centW):
        #        print("Horizontal: Centered")
        #    if (pt[1] > centH):
        #        print("Vertical: Move Down")
        #    elif (pt[1] < centH):
        #        print("Vertical: Move Up")
        #    elif (pt[1] == centH):
        #        print("Vertical: Centered")
        #    else:
        #        print("Landing Pad Not Found")
        #    i = 0;
#    res_5 = cv2.matchTemplate(gray,img_5,eval('cv2.TM_CCOEFF_NORMED'))
#    loc_5 = np.where(res_5 >= threshold)
#    for pt in zip(*loc_5[::-1]):
#        cv2.rectangle(frame, pt, (pt[0]+50, pt[1]+50), (255,0,0), 1)

    #Display the resulting frame
    cv2.imshow('frame', frame)
    #print(i)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#When everything done, release the capture
capture.release()
cv2.destroyAllWindows()

exit()
