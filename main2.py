import cv2

img = cv2.imread('assets/pic.jpg', -1)

print(img)
print(type(img))
print(img.shape)

''' Note Standard use is RGB but OpenCV uses BGR'''

''' [[[214 124  35]
  [214 124  35]
  [214 124  35]
  ...
  [213 125  35]
  [213 125  35]
  [213 125  35]]

 [[214 124  35]
  [214 124  35]
  [214 124  35]
  ...
  [213 125  35]
  [213 125  35]
  [213 125  35]]

 [[213 123  34]
  [213 123  34]
  [213 123  34]
  ...
  [212 124  34]
  [212 124  34]
  [212 124  34]]

 ...

 [[210 117  24]
  [210 117  24]
  [210 117  24]
  ...
  [222 185 147]
  [222 185 147]
  [222 185 147]]

 [[211 118  25]
  [210 117  24]
  [210 117  24]
  ...
  [222 185 147]
  [222 185 147]
  [222 185 147]]

 [[211 118  25]
  [210 117  24]
  [210 117  24]
  ...
  [222 185 147]
  [222 185 147]
  [222 185 147]]]
  
  This is the result we should get when we print this
  and the type we get is <class 'numpy.ndarray'>
  and for the shape it would show something like (900, 1440, 3) where 900 tells me that i have 900 rows(height)
  , 1440 tells me that i have 1440 columns(width) and 3 channels, here channel is just the color space of our image
  
  In this array [214,124,35] this is the color of a pixel where 214 is blue, 124 green and 35 is red
  This is how we can represent in general -->
  blue green red
  [0 ,   0 ,  0] this range exists from 0-255'''

b = img[0]
print(b)
print(type(b))
''' Here in this row we are looking at the first row of the pixels in the image which is something like in the format
of this --->
[[214 124  35]
 [214 124  35]
 [214 124  35]
 ...
 [213 125  35]
 [213 125  35]
 [213 125  35]]
 '''
a = img[250][45:400]
print(a)
print(type(a))
''' Here in this code we are seeint the 250th row in the image and the pixels between 45 to 400 which will be 
something like this --> 
[[212 122  33]
 [212 122  33]
 [212 122  33]
 ...
 [216 129  43]
 [217 130  44]
 [217 130  44]]'''

print(img[250][400])
''' Here we are taking look at just one pixel(in case here 400) from the 250th row of the image which looks like 
this ---> [218 131  45]'''

