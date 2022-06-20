import cv2

img = cv2.imread('assets\pic.jpg', 0)
img = cv2.resize(img, (800,800)) 
'''img is the image we have take and the number are the dimension of the window we want to open into'''
img = cv2.resize(img, (0,0), fx = 0.5, fy = 0.5) 
'''Here if you want to make it half or quater or whatever we want then we will keeep the dimensions 0,0 and wirte fx and fy which are multipled by the number of pixels here 0.5 makes the image half of the size.'''
img = cv2.rotate(img, cv2.cv2.ROTATE_90_CLOCKWISE) 
'''This function makes the imafe rotate counterclockwise by 90 degrees'''

'''-1, cv2.imread_color : Loads a color image. Any transparency of image will be neglected. It is the default flag.
    0, cv2.imread_grayscale : Loads image in grayscale mode
    1, cv2.imread_unchanged : Loads image as such including aplha channels'''

cv2.imwrite('lol.jpg', img)
''' Writes all the changes we have done to this file and saves it with a filename'''

cv2.imshow('Image', img) 
''' Shows the images with the 'Image' being the window named and img being the variable in which the pic is stored and opened'''
cv2.waitKey(0)  
'''Waits for an infinite amount of time for any key to be pressed we can set it as 50 10 etc.'''
cv2.destroyAllWindows() 
'''Destroys all the windows so that nothing is running in the background '''

