from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QSlider
from PyQt5.QtGui import QImage
import cv2 as cv
import numpy as np
import imutils
from skimage import img_as_ubyte,img_as_int
from skimage.filters import (threshold_otsu,
                             threshold_sauvola)




class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(940, 454)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("border: 3px dashed #ccc")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setVisible(False)
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.verticalLayout_2.addWidget(self.comboBox_4)

        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(-1, 16, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.comboBox_5 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.setVisible(False)
        self.verticalLayout_3.addWidget(self.comboBox_5)

        self.horizontalSlider = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.verticalLayout_3.addWidget(self.horizontalSlider)

        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setVisible(False)
        self.verticalLayout_3.addWidget(self.pushButton_5)
        

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 16, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.setVisible(False)
        self.horizontalLayout_2.addWidget(self.comboBox_2)
        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.setVisible(False)
        self.horizontalLayout_2.addWidget(self.comboBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralwidget)
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.horizontalSlider_2.setTickInterval(1)
        self.horizontalSlider_2.setMinimum(0)
        self.horizontalSlider_2.setMaximum(10)
        self.horizontalSlider_2.setTickPosition(QSlider.TicksBothSides)
        self.verticalLayout.addWidget(self.horizontalSlider_2)
        self.verticalLayout.addWidget(self.pushButton_3)

        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 940, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # cacher tous les widgets
        self.comboBox.setVisible(False)
        self.comboBox.setVisible(False)
        self.comboBox.setVisible(False)
        self.horizontalSlider_2.setVisible(False)
        self.pushButton_3.setVisible(False)

        self.retranslateUi(MainWindow)
        self.horizontalSlider.setVisible(False)
        self.horizontalSlider.valueChanged['int'].connect(self.th_value)
        self.horizontalSlider_2.valueChanged['int'].connect(self.filter_value)
        self.pushButton.clicked.connect(self.loadImage)
        self.pushButton_2.clicked.connect(self.saveImage)
        self.pushButton_4.clicked.connect(self.rechargeOriginalImg)
        self.pushButton_3.clicked.connect(self.confirmeFiltre)
        self.pushButton_5.clicked.connect(self.confirmeBinarization)


        actions = ["Binarisation", "Filtrage"]
        self.comboBox_4.addItem("Selectionner une action")
        self.comboBox_4.addItems(actions)

        binarisations = ["OTSU","Seuillage","Sauvola"]
        self.comboBox_5.addItem("Selectionner une technique de binarisation")
        self.comboBox_5.addItems(binarisations)

        filtres = ["filtre moyen", "filtre mediane","filtre gaussien","filtre laplacien","filtres morphologiques"]
        self.comboBox.addItem("Selectionner un filtre")
        self.comboBox.addItems(filtres)

        morphology = ["Erosion", "Dilation","Opening","Closing","Gradient","BlackHat","TopHat"]
        self.comboBox_2.addItem("Selectionner une morphologie")
        self.comboBox_2.addItems(morphology)

        kernel = ["Rect", "Cross","Ellipse"]
        self.comboBox_3.addItem("Selectionner un noyau")
        self.comboBox_3.addItems(kernel)

        self.comboBox.activated[str].connect(self.choiceFilter)
        self.comboBox_2.activated[str].connect(self.choiceMorph)
        self.comboBox_3.activated[str].connect(self.choiceKernel)
        self.comboBox_4.activated[str].connect(self.choiceAction)
        self.comboBox_5.activated[str].connect(self.choiceBinarization)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        #le code ajout??
        self.filename = None
        self.tmp = None
        self.blur = 0
        # self.threshold = None

        self.action_val = None
        self.binarisation_val = None
        self.filter_val = None
        self.morph_val = None 
        self.kernel_val = None


    def choiceBinarization(self,value):
        self.binarisation_val = value
        self.horizontalSlider.setSliderPosition(0)
        if self.binarisation_val == "OTSU" : 
            self.horizontalSlider.setVisible(False)
            self.updateImage()
        else :
            self.horizontalSlider.setVisible(True)
    
    def choiceFilter(self, value):
        self.filter_val = value
        if(self.filter_val != "filtres morphologiques"):
            self.comboBox_2.setVisible(False)
            self.comboBox_3.setVisible(False)
            if(self.filter_val == "filtre laplacien"):
                # self.horizontalSlider.setVisible(False)
                self.horizontalSlider_2.setVisible(False)
                self.updateImage()
            else:
                # self.horizontalSlider.setVisible(True)
                self.horizontalSlider_2.setVisible(True)
        else:
            self.comboBox_2.setVisible(True)
            # self.horizontalSlider.setVisible(False)
            self.horizontalSlider_2.setVisible(True)

    def choiceAction(self,value):
            # self.setPhoto(self.image)
            self.action_val = value
            if(self.action_val == "Binarisation"):
                self.filter_val = None
                self.setPhoto(cv.cvtColor(self.image,cv.COLOR_BGR2GRAY))
                self.pushButton_5.setVisible(True)
                self.comboBox.setCurrentIndex(0)
                self.comboBox_2.setCurrentIndex(0)
                self.comboBox_3.setCurrentIndex(0)
                self.comboBox.setVisible(False)
                self.comboBox_2.setVisible(False)
                self.comboBox_3.setVisible(False)
                self.horizontalSlider_2.setVisible(False)
                self.pushButton_3.setVisible(False)
                self.comboBox_5.setVisible(True)
                self.horizontalSlider.setVisible(True)
                # self.horizontalSlider_2.setSliderPosition(0)

            elif(self.action_val == "Filtrage"):
                self.setPhoto(self.image)
                self.comboBox.setVisible(True)
                self.horizontalSlider_2.setVisible(True)
                self.pushButton_3.setVisible(True)
                self.comboBox_5.setVisible(False)
                self.horizontalSlider.setVisible(False)
                self.comboBox_5.setCurrentIndex(0)
                self.pushButton_5.setVisible(False)
                self.binarisation_val = None


    def choiceMorph(self, value):
        self.morph_val = value
        if(self.morph_val != None) and (self.morph_val != "Selectionner une morphologie"):
            self.comboBox_3.setVisible(True)
            if(self.kernel_val!=None and self.kernel_val!="Selectionner un noyau"):
                self.updateImage()
        else:
            self.comboBox_3.setVisible(False)
     
        

    def choiceKernel(self, value):
        self.kernel_val = value
        if(self.kernel_val!=None and self.kernel_val!="Selectionner un noyau"):
            if(self.morph_val != None) and (self.morph_val != "Selectionner une morphologie"):
                self.updateImage()
    

    def loadImage(self):
        # pour t??l??charger l'image s??lectionn??e
        self.filename = QFileDialog.getOpenFileName(filter="Image (*.*)")[0]
        self.image = cv.imread(self.filename,cv.IMREAD_UNCHANGED)
        self.original_img = self.image
        self.pushButton_4.setVisible(True)
        self.setPhoto(self.image)

    def saveImage(self):
        cv.imwrite(self.filename,self.tmp)

    
    def rechargeOriginalImg(self):
        self.image = self.original_img
        self.setPhoto(self.image)


    def setPhoto(self,image):
        # prendre l'image et la redimentionn??e
        self.tmp = image
        image = imutils.resize(image,width=640)
        frame = cv.cvtColor(image,cv.COLOR_BGR2RGB)
        image = QImage(frame, frame.shape[1],frame.shape[0], frame.strides[0], QImage.Format_RGB888)
        self.label.setPixmap(QtGui.QPixmap.fromImage(image))

    def confirmeBinarization(self):
        self.image = self.tmp
        self.binarisation_val = None
        self.comboBox_5.setCurrentIndex(0)
        self.horizontalSlider.setSliderPosition(0)

    def confirmeFiltre(self):
        self.image = self.tmp
        self.comboBox.setCurrentIndex(0)
        self.comboBox_2.setCurrentIndex(0)
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_2.setVisible(False)
        self.comboBox_3.setVisible(False)
        self.filter_val = None
        self.morph_val = None 
        self.kernel_val = None
        self.horizontalSlider_2.setSliderPosition(0)

    def th_value(self,value):
        self.threshold = int((value*255)/100)
        self.updateImage()

    def filter_value(self):
        self.blur = self.horizontalSlider_2.value()
        self.updateImage()


    def changeTh(self,img,value):
        imgRes = np.zeros(img.shape,np.uint8)
        cv.threshold(img,value,255,0,imgRes)
        return imgRes

    def changeSauvola(self,img,size):
        if (size % 2 != 0):
            thresh_sauvola = threshold_sauvola(img, window_size=size)
        else:
           thresh_sauvola = threshold_sauvola(img, window_size=size+1)

        binary_sauvola = img > thresh_sauvola
        binary_sauvola = img_as_ubyte(binary_sauvola)
        return binary_sauvola

    


    def changeOTSU(self,img):
        binary_global = img > threshold_otsu(img)
        binary_global = img_as_ubyte(binary_global)
        return binary_global

    def filtreMoyen(self,img,size):
        kernel_size = (size+1 , size+1)
        image = cv.blur(img,kernel_size)
        return image


    def filtreMedian(self,img,size):
        if (size % 2 != 0):
            image = cv.medianBlur(img,size)
        else:
            image = cv.medianBlur(img,size+1)
        return image


    def filtreGaussian(self,img,size):
        if (size % 2 != 0):
            image = cv.GaussianBlur(img,(size , size),0)
        else:
            image = cv.GaussianBlur(img,(size+1 , size+1),0)
        return image

    def filtreLaplacian(self,img):
        image = cv.Laplacian(img, cv.CV_16S, ksize=3)
        image = cv.convertScaleAbs(image)
        return image

    def filtreMorpho(self,image,filtre,shape,tailleNoyau):
        #creer un noyau
        if tailleNoyau == 0:
            tailleNoyau = 1

        if shape=="Rect":
            noyau = (cv.getStructuringElement(cv.MORPH_RECT,(tailleNoyau,tailleNoyau)))
        elif shape=="Ellipse":
            noyau = (cv.getStructuringElement(cv.MORPH_ELLIPSE,(tailleNoyau,tailleNoyau)))
        elif shape=="Cross":
            noyau = (cv.getStructuringElement(cv.MORPH_CROSS,(tailleNoyau,tailleNoyau)))

        #initialiser l'image filtr??e
        filtredImage=np.zeros((image.shape[0],image.shape[1],3), np.uint8)
        #Appliquer les filtres
        if filtre=="Erosion":        
            filtredImage = cv.erode(image,noyau)
        elif filtre =="Dilation":
            filtredImage = cv.dilate(image,noyau)
        elif filtre =="Opening":
            filtredImage = cv.morphologyEx(image,cv.MORPH_OPEN,noyau)
        elif filtre =="Closing":
            filtredImage = cv.morphologyEx(image,cv.MORPH_CLOSE,noyau)
        elif filtre =="Gradient":
            filtredImage = cv.morphologyEx(image,cv.MORPH_GRADIENT,noyau)
        elif filtre =="BlackHat":
            filtredImage = cv.morphologyEx(image,cv.MORPH_BLACKHAT,noyau)
        elif filtre =="TopHat":
            filtredImage = cv.morphologyEx(image,cv.MORPH_TOPHAT,noyau)
        return filtredImage


    def updateImage(self):
        if self.filter_val != "Selectionner un filtre":
            if self.filter_val == "filtre moyen":
                img = self.filtreMoyen(self.image,self.blur)
                # img = self.changeTh(img,self.threshold)
                self.setPhoto(img)
            elif self.filter_val == "filtre mediane":
                img = self.filtreMedian(self.image,self.blur)
                # img = self.changeTh(img,self.threshold)
                self.setPhoto(img)
            elif self.filter_val == "filtre gaussien":
                img = self.filtreGaussian(self.image,self.blur)
                # img = self.changeTh(img,self.threshold)
                self.setPhoto(img)
            elif self.filter_val == "filtre laplacien":
                img = self.filtreLaplacian(self.image)
                self.setPhoto(img)
            elif self.filter_val == "filtres morphologiques":
                if(self.morph_val!=None and self.morph_val!="Selectionner une morphologie") and (self.kernel_val!=None and self.kernel_val!="Selectionner un noyau"):
                    img = self.filtreMorpho(self.image,self.morph_val,self.kernel_val,self.blur)
                    self.setPhoto(img)
        
        if self.binarisation_val != "Selectionner une technique de binarisation":
            if self.binarisation_val == "Seuillage":
                img = cv.cvtColor(self.image,cv.COLOR_BGR2GRAY)
                img = self.changeTh(img,self.threshold)
                self.setPhoto(img)
            if self.binarisation_val == "Sauvola":
                img = cv.cvtColor(self.image,cv.COLOR_BGR2GRAY)
                img = self.changeSauvola(img,self.threshold)
                self.setPhoto(img)
        
            if self.binarisation_val == "OTSU":
                img = cv.cvtColor(self.image,cv.COLOR_BGR2GRAY)
                img = self.changeOTSU(img)
                self.setPhoto(img)
                
                

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "T??lecharger une image"))
        self.pushButton.setText(_translate("MainWindow", "Ouvrir une image"))
        self.pushButton_2.setText(_translate("MainWindow", "Sauvgarder l\'image"))
        self.pushButton_3.setText(_translate("MainWindow", "Confirmer le filtre"))
        self.pushButton_4.setText(_translate("MainWindow", "Recharger l'image originale"))
        self.pushButton_5.setText(_translate("MainWindow", "Confirmer la binarisation"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
