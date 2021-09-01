# import cv2 library
import cv2
import random

# read the images
img1 = cv2.imread('images/1.png')
img2 = cv2.imread('images/2.png')
img3 = cv2.imread('images/3.png')
img4 = cv2.imread('images/4.png')
img5 = cv2.imread('images/5.png')
img6 = cv2.imread('images/6.png')
img_logo = cv2.imread('images/logo.png')
randomlst = [random.randint(1, 6) for x in range(23)]

img_list = [img_logo]
for item in randomlst:
    num = int(item)
    if num == 1:
        img_list.append(img1)
    elif num == 2:
        img_list.append(img2)
    elif num == 3:
        img_list.append(img3)
    elif num == 4:
        img_list.append(img4)
    elif num == 5:
        img_list.append(img5)
    elif num == 6:
        img_list.append(img6)


# show the output image
code = cv2.hconcat(img_list)
cv2.imshow('randomSpotifyCode.png', code)

cv2.waitKey(0)
