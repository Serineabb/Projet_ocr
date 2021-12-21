import cv2
import numpy as np

#import matplotlib.pyplot as plt

img = cv2.imread('image3.jpg',cv2.IMREAD_COLOR)


voisinage=5
def filtrem(img,tailleBloc):
    kernel = np.ones((tailleBloc,tailleBloc),np.float32)/(tailleBloc*tailleBloc)
    imgMoy = cv2.filter2D(img,-1,kernel)
    '''h,w,c =img.shape 
    imgMoy=np.zeros(img.shape,np.float64)
    for y in range(h):
        for x in range(w):
            if x<voisinage/2 or x>w-voisinage/2 or y<voisinage/2 or y>h-voisinage/2:
             imgMoy[y,x] = img[y,x]         
            else:
               imgV=img[int(y-voisinage/2):int(y+voisinage/2)+1,int(x-voisinage/2):int(y+voisinage/2)+1]
               imgMoy[y,x]=np.mean(imgV)'''
    return imgMoy
def filtremediane(img):
    image = cv2.medianBlur(img,3)
    return image
def filtrevoisinage(image,voisinage):
 image= cv2.imread('image3.jpg',cv2.IMREAD_GRAYSCALE)
 h,w = image.shape
 imgRes = np.zeros(image.shape, np.uint8)

 

 for y in range(h):
    for x in range(w):
        if x<voisinage/2 or x>w-voisinage/2 or y<voisinage/2 or y>h-voisinage/2:
            imgRes[y,x] = image[y,x]
        else:
            imgv = image[int(y-voisinage/2):int(y+voisinage/2)+1,int(x-voisinage/2):int(x+voisinage/2)+1]
            imgRes[y,x] = np.mean(imgv)
 return imgRes

def filtreMorpho(image,filtre,shape,tailleNoyau):

    #creer un noyau
    if shape=="Rect":
        noyau = (cv2.getStructuringElement(cv2.MORPH_RECT,(tailleNoyau,tailleNoyau)))
    elif shape=="Ellipse":
        noyau = (cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(tailleNoyau,tailleNoyau)))
    elif shape=="Cross":
        noyau = (cv2.getStructuringElement(cv2.MORPH_CROSS,(tailleNoyau,tailleNoyau)))

    #initialiser l'image filtré
    filtredImage=np.zeros((image.shape[0],image.shape[1],3), np.uint8)
    #Appliquer les filtres
    if filtre=="Erosion":        
        filtredImage = cv2.erode(image,noyau)
    elif filtre =="Dilation":
        filtredImage = cv2.dilate(image,noyau)
    elif filtre =="Opening":
        filtredImage = cv2.morphologyEx(image,cv2.MORPH_OPEN,noyau)
    elif filtre =="Closing":
        filtredImage = cv2.morphologyEx(image,cv2.MORPH_CLOSE,noyau)
    elif filtre =="Gradient":
        filtredImage = cv2.morphologyEx(image,cv2.MORPH_GRADIENT,noyau)
    elif filtre =="BlackHat":
        filtredImage = cv2.morphologyEx(image,cv2.MORPH_BLACKHAT,noyau)
    elif filtre =="TopHat":
        filtredImage = cv2.morphologyEx(image,cv2.MORPH_TOPHAT,noyau)
    return filtredImage

#imgg=filtrem(img,5)
imgMoy=filtrevoisinage(img,1)


cv2.imshow("original",img)
cv2.imshow("filitre moyenneur",imgMoy)
cv2.waitKey(0)
