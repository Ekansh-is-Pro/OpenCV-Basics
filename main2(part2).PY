import cv2
import random
import time
import cv2


def editor():
    img = cv2.imread('assets/pic.jpg', -1)
    for i in range(100):
        for j in range(img.shape[1]):
            img[i][j] = [random.randint(0,255), random.randint(0,255), random.randint(0,255)]
            ''' Here in the above code we are selecting the first 100 rows and then modifying each pixel by modifying it's
            channels thereby changing the color of that part of the image'''
    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


editor()