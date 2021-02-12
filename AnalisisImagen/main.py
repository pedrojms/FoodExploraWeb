import cv2
import numpy as np
import math

#CIRCULO DEL PLATO DE COMIDA
#Detectando el circulo del plato de comida
imagen = cv2.imread('Platoreal4.jpg')
cv2.imshow('Imagen',imagen)
img_gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

# Detect edges in the image. The parameters control the thresholds
blur = cv2.GaussianBlur(img_gris,(5,5),0)

edges = cv2.Canny(img_gris, 50, 150, apertureSize=3)

rows = img_gris.shape[0]
circles = cv2.HoughCircles(img_gris,cv2.HOUGH_GRADIENT,1.5,rows,param1=50,param2=20,minRadius=10,maxRadius=300)

#Enmascarando
circles = np.uint16(np.around(circles))
masking=np.full((imagen.shape[0], imagen.shape[1]),0,dtype=np.uint8)

lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 150, 0, minLineLength=10, maxLineGap=200)
print(lines)
mask1 = np.zeros(imagen.shape, np.uint8)
h,w= imagen.shape[0:2]
print("algo",(h,w))

for i in circles[0,:]:
    centrox= i[0]
    centroy= i[1]
    radio=i[2]
    angulo=0
    angulo2=90
    angulo3=270
    # Dibuja la circusnferencia del círculo
    cv2.circle(masking,(centrox,centroy),radio,(255,255,0),-1)
    # LINEAS DENTRO DEL PLATO

#CONTEO DE PIXELES NO NEGROS EN LA IMAGEN ANTES DE REDUCIR COLORES

final_img = cv2.bitwise_or(imagen, imagen, mask=masking)


height, width, _ = final_img.shape
print(height,width)
cv2.imshow('Plato',final_img)
tpix=0
for i in range(height):
    for j in range(width):
        if all(final_img[i,j]!=(0,0,0)):
            tpix+=1

if lines is not None:
    for line in lines:
        x1, y1, x2, y2 = line[0]
        pt1 = (x1, y1)
        pt2 = (x2, y2)
        cv2.line(final_img, pt1, pt2, (0, 0, 0), 3)
        poly= np.array([pt1,pt2,[w,0],[w,h],[x1,h],],dtype=np.int32)
        cv2.fillPoly(final_img,[poly],(0,0,0))


#REDUCCION DE COLORES CON KMEANS
Z = final_img.reshape((-1,3))
# convert to np.float32
Z = np.float32(Z)
# define criteria, number of clusters(K) and apply kmeans()
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10, 1.0)
K = 3
ret,label,center=cv2.kmeans(Z,K,None,criteria,10,cv2.KMEANS_RANDOM_CENTERS)
# Now convert back into uint8, and make original image
center = np.uint8(center)
res = center[label.flatten()]
final_img = res.reshape(final_img.shape)

#mascara sin blancos



#CONTANDO LA CANTIDAD DE PIXELES NO NEGROS DESPUES DE REDUCIR COLORES
height, width, _ = final_img.shape
print(height,width)
tveg= 0

darkest_color= [255,255,255]
for i in range(height):
    for j in range(width):
        if all(final_img[i, j] != (0, 0, 0)):
            if np.all(final_img[i,j] < darkest_color ):
                darkest_color=final_img[i,j]
print(darkest_color)
for i in range(height):
    for j in range(width):
        if all(final_img[i, j] == darkest_color):
            tveg+=1


print("Pixeles vegetales:",tveg)
print("Pixeles totales:",tpix)
porcentaje=str(round(((tveg/tpix)*100)))+'%'

#SHOWING IMAGES
cv2.putText(final_img,porcentaje,(30,30),cv2.FONT_HERSHEY_SIMPLEX,1,(255,255,255),3,cv2.LINE_AA)
cv2.imshow('Analisis',final_img)
cv2.waitKey()
