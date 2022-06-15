import cv2

img = cv2.imread('assets\pic.jpg', -1)

tag = img[500:700, 450:950]
img[100:450 , 500:900] = tag

''' Here we are slicing the array in first part and locating the pixels we want to replace in the first part
in the second part we are selecting our pixels we want to copy and paste them into the picture then by
providing the range between which the pixels can be pasted

Unfortuantly I've still failed to solve this error givgin me
    img[100:450 , 500:900] = tag
ValueError: could not broadcast input array from shape (200,500,3) into shape (350,400,3)

So please someone help me soelve this trash :) '''

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()