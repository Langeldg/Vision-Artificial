import cv2
import numpy as np

img=np.zeros((500,800,3),np.uint8)

img=cv2.rectangle(img, (180,40), (600,460), (255,0,0), 5)

img=cv2.circle(img, (400,250), 200, (199,21,133),5)

pts=np.array([[400,60],[590,250],[400,440],[210,250]],np.int32)
pts=pts.reshape((-1,1,2))
cv2.polylines(img,[pts], True, (255,192,203),5)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, '2', (10,30), font, 1, (216,191,216),2)

frac=img[30:340, 410:630]

cv2.imshow('1', img)
cv2.imshow('2', frac)

cv2.waitKey(0)
cv2.destroyAllWindows()
