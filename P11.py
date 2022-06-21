import cv2
import matplotlib.pyplot as plt
import numpy as np


#SIMILITUDES EN OTRA IMAGEN

#Homografia de imagenes
imag1 = cv2.imread(r'C:\Users\chato\OneDrive\Escritorio\Vision Artificial\6.jpg',0)
imag2 = cv2.imread(r'C:\Users\chato\OneDrive\Escritorio\Vision Artificial\7.jpg',0)

orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(imag1,None)
kp2, des2 = orb.detectAndCompute(imag2,None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1,des2)
matches = sorted(matches, key = lambda x:x.distance)

imag3 = cv2.drawMatches(imag1,kp1,imag2,kp2,matches[:12],None,flags=2)

cv2.imshow('Imagen de coincidencias', imag3)


#EXTRACCIÓN DE FONDO EN VIDEO

#Funcion MOG
video = cv2.VideoCapture(r'C:\Users\chato\Videos\History.mp4')
ext_fondo = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = video.read()

    mascara = ext_fondo.apply(frame)
 
    cv2.imshow('Video Original',frame)
    cv2.imshow('Extraccion de Fondo',mascara)

    
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
    

video.release()

cv2.waitKey(0)

cv2.destroyAllWindows()
