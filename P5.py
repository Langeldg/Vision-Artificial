import cv2
import numpy as np

img=cv2.imread('3.jpg')

cad, umbral=cv2.threshold(img, 12,255, cv2.THRESH_BINARY)

gris=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cad2, umbral2=cv2.threshold(gris, 12,255, cv2.THRESH_BINARY)
gaus=cv2.adaptiveThreshold(gris, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115,1)

cad2, otsu=cv2.threshold(gris, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cad3,umbral3 = cv2.threshold(gris,255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_TRUNC)

cad4,umbral4 = cv2.threshold(gris, 127 ,200,cv2.THRESH_TOZERO_INV)

#cv2.imshow('original', img)
cv2.imshow('umbral', umbral)
cv2.imshow('umbral2', umbral2)
cv2.imshow('gaus', gaus)
cv2.imshow('OTSU', otsu)
cv2.imshow('trunc', umbral3)
cv2.imshow('TOZERO_INV', umbral4)
