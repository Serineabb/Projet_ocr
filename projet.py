import cv2
import numpy as np
#import matplotlib.pyplot as plt

img = cv2.imread('image2.jpg',cv2.IMREAD_GRAYSCALE)
voisinage=5
def filtrem(img):
    h,w =img.shape
    imgMoy=np.zeros(img.shape,np.uint64)
    for y in range(h):
        for x in range(w):
            if x<voisinage/2 or x>w-voisinage/2 or y<voisinage/2 or y>h-voisinage/2:
             imgMoy[y,x] = img[x,x]

            
            else:
               imgV=img[int(y-voisinage/2):int(y+voisinage/2)+1,int(x-voisinage/2):int(y+voisinage/2)+1]
               imgMoy[y,x]=np.median(imgV)
    return imgMoy

def QIR(img,A,C):
    h,w = img.shape
    for i in range(h):
        for j in range(w):
            if(img[i,j]<=A):
                img[i,j]=0
            elif(img[i,j]>=C):
                img[i,j]=255
    cv2.imwrite("QIR/A :"+str(A)+" et C :"+str(C)+".png", img)
    
img = cv2.imread("C:/Users/Yasmine/Desktop/image processing/OCR/Projet/projet I/image4.jpg", cv2.IMREAD_GRAYSCALE)

C=140
for A in range(20,130):
    QIR(img,A,C)
A=20
for A in range(140,255):
    QIR(img,A,C)
'''imgMoy=filtrem(img)
cv2.imshow("kek",img)
cv2.waitKey(0)'''
