import matplotlib.pyplot as plt
import pylab
import cv2
import numpy as np

#Imagen 
imagen = plt.imread ("5.jpg") 

#Kernel
enfoque = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [ 0, -1, 0]])

tam=5
media = np.ones((tam,tam))/(tam**2)
                  
bordes = np.array([[-1, -1, -1],
                    [-1, 8, -1],
                    [-1, -1, -1]])   

realce = np.array([[-1, -1, 0], 
                   [-1, 0, 1],
                   [0, 1, 1]])                                                   

conv_enf = cv2.filter2D(imagen, -1, enfoque) 
conv_med = cv2.filter2D(imagen, -1, media)
conv_bor = cv2.filter2D(imagen, -1, bordes) 


plt.subplot(2,2,1)
plt.imshow (imagen)
plt.title('Imagen Original')
plt.axis('off')
 
plt.subplot(2,2,2)
plt.imshow (conv_enf)
plt.title('Enfoque')
plt.axis('off')

plt.subplot(2,2,3)
plt.imshow (conv_med)
plt.title('Media')
plt.axis('off')

plt.subplot(2,2,4)
plt.imshow (conv_bor)
plt.title('Filtro')
plt.axis('off') 

pylab.show()
