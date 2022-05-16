import cv2
import numpy as np
from matplotlib import pyplot as plt

def imprimir_graficas1(img, y, nombre):
    #plt.subplot(y,x,1)
    #plt.title("Original")
    axes[0, y].imshow(img)
    axes[0, y].set_title(nombre)
    
    g = img[:,:,0]
    b = img[:,:,1]
    r = img[:,:,2]

    r2 = cv2.equalizeHist(r)
    g2 = cv2.equalizeHist(g)
    b2 = cv2.equalizeHist(b)

    im2 = img.copy()
    im2[:,:,0] = g2
    im2[:,:,1] = b2
    im2[:,:,2] = r2

    color = ('b','g','r')
    for i, c in enumerate(color):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        #plt.subplot(y,x,2)
        #plt.plot(hist, color = c)
        #plt.title("Histograma")
        #plt.xlim([0,256])
        axes[1, y].set_title("Histograma")
        axes[1, y].plot(hist, color = c)

        hist2 = cv2.calcHist([im2], [i], None, [256], [0, 256])
        #plt.subplot(y,x,3)
        #plt.plot(hist2, color = c)
        #plt.title("Ecualizado")
        #plt.xlim([0,256])
        axes[2, y].set_title("Ecualizado")
        axes[2, y].plot(hist2, color = c)
        
    #plt.subplot(y,x,4)
    #plt.title("Ecualizada")
    axes[3, y].imshow(im2)
    axes[3, y].set_title("Ecualizada")

def imprimir_graficas2(img, y, nombre):
    #plt.subplot(y,x,1)
    #plt.title("Original")
    axes1[0, y].imshow(img)
    axes1[0, y].set_title(nombre)
    
    g = img[:,:,0]
    b = img[:,:,1]
    r = img[:,:,2]

    r2 = cv2.equalizeHist(r)
    g2 = cv2.equalizeHist(g)
    b2 = cv2.equalizeHist(b)

    im2 = img.copy()
    im2[:,:,0] = g2
    im2[:,:,1] = b2
    im2[:,:,2] = r2

    color = ('b','g','r')
    for i, c in enumerate(color):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        #plt.subplot(y,x,2)
        #plt.plot(hist, color = c)
        #plt.title("Histograma")
        #plt.xlim([0,256])
        axes1[1, y].set_title("Histograma")
        axes1[1, y].plot(hist, color = c)

        hist2 = cv2.calcHist([im2], [i], None, [256], [0, 256])
        #plt.subplot(y,x,3)
        #plt.plot(hist2, color = c)
        #plt.title("Ecualizado")
        #plt.xlim([0,256])
        axes1[2, y].set_title("Ecualizado")
        axes1[2, y].plot(hist2, color = c)
        
    #plt.subplot(y,x,4)
    #plt.title("Ecualizada")
    axes1[3, y].imshow(im2)
    axes1[3, y].set_title("Ecualizada")

def imprimir_graficas3(img, y, nombre):
    #plt.subplot(y,x,1)
    #plt.title("Original")
    axes2[0, y].imshow(img)
    axes2[0, y].set_title(nombre)
    
    g = img[:,:,0]
    b = img[:,:,1]
    r = img[:,:,2]

    r2 = cv2.equalizeHist(r)
    g2 = cv2.equalizeHist(g)
    b2 = cv2.equalizeHist(b)

    im2 = img.copy()
    im2[:,:,0] = g2
    im2[:,:,1] = b2
    im2[:,:,2] = r2

    color = ('b','g','r')
    for i, c in enumerate(color):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        #plt.subplot(y,x,2)
        #plt.plot(hist, color = c)
        #plt.title("Histograma")
        #plt.xlim([0,256])
        axes2[1, y].set_title("Histograma")
        axes2[1, y].plot(hist, color = c)

        hist2 = cv2.calcHist([im2], [i], None, [256], [0, 256])
        #plt.subplot(y,x,3)
        #plt.plot(hist2, color = c)
        #plt.title("Ecualizado")
        #plt.xlim([0,256])
        axes2[2, y].set_title("Ecualizado")
        axes2[2, y].plot(hist2, color = c)
        
    #plt.subplot(y,x,4)
    #plt.title("Ecualizada")
    axes2[3, y].imshow(im2)
    axes2[3, y].set_title("Ecualizada")

#definir subplots

figure, axes=plt.subplots(nrows=4, ncols=4, figsize=(10,10))
figure1, axes1=plt.subplots(nrows=4, ncols=4, figsize=(10,10))
figure2, axes2=plt.subplots(nrows=4, ncols=5, figsize=(10,10))

#lectura de imagenes
img = cv2.imread("1.jpg")
img=cv2.resize(img, dsize=(300,500))
img2= cv2.imread("1.jpg")
img2=cv2.resize(img2, dsize=(300,500))


#imprimir imgen OG
imprimir_graficas1(img, 0, "Original")

#operaciones

#suma
suma=img+img2
imprimir_graficas1(suma, 1, "suma")

#resta
resta=img-img2
imprimir_graficas1(resta, 2, "resta")

#multiplicacion
multi=img*img2
imprimir_graficas1(multi, 3, "Multiplicación")

#division
#div=img/img2
#imprimir_graficas(div, 4)

#logaritmo
arr = 255 / np.log(1 + np.max(img))
resp4 = arr * (np.log(img + 1))
resp4 = np.array(resp4, dtype = np.uint8)
#raiz
raiz=img2** -img
imprimir_graficas2(raiz, 0, "Raiz")
#derivada
deriv=cv2.Laplacian(resp4,cv2.CV_64F)
#potencia
potencia=img2**img
imprimir_graficas2(potencia, 1, "Potencia")
#imprimir_graficas(1,potencia, 0)
#conjuncion
conjuncion= cv2.bitwise_and(img2,img)
imprimir_graficas2(conjuncion, 2, "Conjunción")
#disyuncion
disyuncion=cv2.bitwise_or(img2,img)
imprimir_graficas2(disyuncion, 3, "Disyunción")
#traslacion
M = np.float32([[1,0,100],[0,1,150]])
traslacion = cv2.warpAffine(img2,M,(img2.shape[1],img2.shape[0]))
imprimir_graficas3(traslacion, 0, "Traslación")
#escalado
escalado=cv2.resize(img,(900,500))
imprimir_graficas3(escalado, 1, "Escalar")
#rotancion
M = cv2.getRotationMatrix2D((img.shape[1]//2,img.shape[0]//2),15,1)
rotacion = cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))
imprimir_graficas3(rotacion, 2, "Rotación")
#a fin
filas,columnas = img2.shape[:2]
pts1 = np.float32([[50,50],[200,50],[50,200]])
pts2 = np.float32([[10,100],[200,50],[100,250]])
M = cv2.getAffineTransform(pts1,pts2)
afin = cv2.warpAffine(img2,M,(filas,columnas))
imprimir_graficas3(afin, 3, "A Fin")
#transpuesta
trans=cv2.transpose(img2)
imprimir_graficas3(trans, 4, "Transpuesta")

figure.tight_layout()
figure1.tight_layout()
figure2.tight_layout()
plt.show()



cv2.waitKey(0)
cv2.destroyAllWindows()
