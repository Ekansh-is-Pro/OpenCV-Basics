import cv2
import numpy as np

''' Target - 
1. Use our webcam to capture image using cv2
2. Duplicate the image 4 times 
3. Rotate those images and put them all into 1 image and then display that.
    NOTE - We can't replicate this same thine with a video file!!'''

cap = cv2.VideoCapture(0) 
'''Here 0 is telling how many cameras it is acessing for eg 0 means 1 webcam here '''
''' We can also use a video for such cases by writing the file name instead of 0'''

while True:
    ret, frame = cap.read()
    '''Here 'ret' tells us wheather the capture device is working properly by returning true or false and frame is the indivisual frame here '''
    #image = np.zeros(frame.shape, np.uint8)
    cv2.imshow('frame', frame)
    #smaller_frame = cv2.resize(frame,(0,0),fx= 0.5,fy=0.5)
    if cv2.waitKey(1) == ord('q'): 
        break
        ''' Here 'ord' means ordinal value of q which is in ASCII and here waitkey() function is waiting for around 1 milisecond'''

cv2.release() #It releases the camera so that another program can now use it 
cv2.destroyAllWindows()