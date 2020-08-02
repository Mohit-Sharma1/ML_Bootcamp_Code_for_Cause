from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

import cv2

frame= cv2.imread("Thor.jpg")

plt.imshow(frame)

rgb=cv2.cvtColor(free,cv2.COLOR_BGR2RGB)   #this is used to
plt.imshow(rgb)

classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

faces=classifier.detectMultiScale(frame)

face=faces[0]

x,y,w,h=face

faces= rgb[y:y+h,x:x+h]

out=cv2.rectangle(rgb,(x,y),(x+w,y+h),(0,0,255),4)

plt.imshow(out)