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
img = cv2.imread('images/Launchpad.png', 0)
img7 = cv2.resize(img, (700, 700),
    interpolation = cv2.INTER_NEAREST)
img6 = cv2.resize(img, (600, 600),
    interpolation = cv2.INTER_NEAREST)
img5 = cv2.resize(img, (500, 500),
    interpolation = cv2.INTER_NEAREST)
img4 = cv2.resize(img, (400, 400),
    interpolation = cv2.INTER_NEAREST)
img3 = cv2.resize(img, (300, 300),
    interpolation = cv2.INTER_NEAREST)
img2 = cv2.resize(img, (200, 200),
    interpolation = cv2.INTER_NEAREST)
img1 = cv2.resize(img, (100, 100),
    interpolation = cv2.INTER_NEAREST)
img_5 = cv2.resize(img, (50, 50),
    interpolation = cv2.INTER_NEAREST)
w, h = img.shape[::-1]
threshold = 0.84
#lowersize = 0.1
#uppersize = 2.5
#step = 0.1
#steps = int((uppersize-lowersize)/step)

#cv2.imshow('reference', img)

while(True):
    #Capture frame-by-frame
    ret, frame = cap.read()

    #Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #op = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            #cv2.THRESH_BINARY,11,2)
    #for x in range(0, steps):
    #    scale = lowersize+(x*step)
    #    simg = cv2.resize(fimg, (int(w*scale), int(h*scale)),
    #            interpolation = cv2.INTER_NEAREST)
    res = cv2.matchTemplate(gray,img,eval('cv2.TM_CCOEFF_NORMED'))
    loc = np.where(res >= threshold)
    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame, pt, (pt[0]+w, pt[1]+h), (255,0,0), 1)

    #Display the resulting frame
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#When everything done, release the capture
capture.release()
cv2.destroyAllWindows()

exit()
