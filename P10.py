import cv2 as cv
import numpy as np
from cmath import rect

img= cv.imread('7.jpg')
roi= cv.selectROI(img)#(x,y,a,h)
mask= np.zeros(img.shape[:2],np.uint8)

bgdModel= np.zeros((1,65),np.float64)
fgdModel= np.zeros((1,65),np.float64)

rect= roi
cv.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv.GC_INIT_WITH_RECT)

mask2= np.where((mask==2)|(mask==0),0,1).astype('uint8')
img= img*mask2[:,:,np.newaxis]

#ESQUINAS
gray= cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray= np.float32(gray)

corner= cv.goodFeaturesToTrack(gray,40,0.01,10)
corner= np.int0(corner)
for i in corner:
    x,y= i.ravel()
    cv.circle(img,(x,y),3,255,-1)

img_cut= img[int(roi[1]):int(roi[1]+roi[3]),int(roi[0]):int(roi[0]+roi[2])]
cv.imshow("Result",img_cut)

cv.waitKey(0)
cv.destroyAllWindows()
