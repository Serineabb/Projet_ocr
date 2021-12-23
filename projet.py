import cv2
import numpy as np
from scipy.ndimage import interpolation as inter
from skimage.filters import (threshold_otsu, threshold_niblack, threshold_sauvola)
from PIL import Image as im
#import bottleneck as bn

#import matplotlib.pyplot as plt

img = cv2.imread('image3.jpg',cv2.COLOR_BGR2GRAY)


voisinage=5
def filtrem(img,tailleBloc):
    kernel = np.ones((tailleBloc,tailleBloc),np.float32)/(tailleBloc*tailleBloc)
    imgMoy = cv2.filter2D(img,-1,kernel)
    return imgMoy

def filtremediane(img):
    image = cv2.medianBlur(img,3)
    return image

def filtre2d():
 img = cv2.imread("rr.jpg",cv2.IMREAD_GRAYSCALE)
 kernel = np.array([
    [1 , 2 , 1] ,
    [2,  4 ,2] ,
    [1 , 2 , 1] 
 ])

 kernel = kernel /16

 imgRes = cv2.filter2D(img,-1,kernel)
 return imgRes

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

def binsauv(img):
 window_size= 25
 thresh_niblack = threshold_niblack(img, window_size=window_size, k=0.8)
 thresh_sauvola = threshold_sauvola(img, window_size=window_size)

 binary_global = img > threshold_otsu(img)
 binary_niblack = img > thresh_niblack
 binary_sauvola = img > thresh_sauvola
 return thresh_sauvola

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
    # technique de binairisation 
def binary_otsus(image, filter:int=1):
    """Binarize an image 0's and 255's using Otsu's Binarization"""
    image = cv2.cvtColor(image,cv2.IMREAD_GRAYSCALE)
    if len(image.shape) == 3:
        gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray_img = image

    # Otsus Binarization
    if filter != 0:
        blur = cv2.GaussianBlur(gray_img, (3,3), 0)
        binary_img = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
    else:
        binary_img = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)[1]
    
    # Morphological Opening
    # kernel = np.ones((3,3),np.uint8)
    # clean_img = cv.morphologyEx(binary_img, cv.MORPH_OPEN, kernel)

    return binary_img



imgv=filtrevoisinage(img,)
imgg=binary_otsus(img,0)




cv2.imshow("binaire sauv",imgg)
cv2.imshow("original",img)
#cv2.imshow("filitre moyenneur",img)
#cv2.imshow("binaire otus",imgs)
cv2.waitKey(0)
