#!/usr/bin/env python
import urllib.request #to get url request
from PyQt5 import QtGui, QtWidgets # Import the PyQt5 module we'll need
from PyQt5.QtWidgets import QLabel,QApplication,QGraphicsBlurEffect, QMessageBox, QWidget, QInputDialog, QLineEdit, QFileDialog,QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon, QImage, QPixmap
from PyQt5.QtCore import QCoreApplication, QUrl, QDate, QSize,Qt
from PIL import Image
from PIL.ImageQt import ImageQt
import sys # We need sys so that we can pass argv to QApplication
import os
import design
import settings
import re
import validators


class PhotoSelector(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self,settings):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined
        self.key1=''
        self.key2=''
        self.key3=''
        self.key4=''
        self.key5=''
        self.loadSettings()        
        self.setImageBlur()
        
        self.settingsSetup=settings
        self.settingsButton.clicked.connect(self.openSettings)
        self.instructionButton.clicked.connect(self.openInstructions)
    
    def openInstructions(self):
        msg=QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle('Instruction')
        msg.setText('Chasefraizer Speaker Lightboard v1.0')
        #msg.setInformativeText('All rights reserved')
        msg.setStandardButtons(QMessageBox.Ok)
        instruction='''
            This tool serves as a speaker lightboard.
            Just press the mapped key for each of the photos and
            the photos will be unblurred.
            The number of photos can be adjusted ranges from 1 to 5
            
            The photos and the keyboard keys can be changed from the settings
            **INSTRUCTION ON UPDATING PHOTOS AND KEYS**
            - Only alphanumeric keys can be assigned for each photo
            - If you want to keep a photo slot inactive, type - in both
            photo path and key path
            - The tmp folder holds the current GUI photo manipulation.
            It is important
            - The settings.dc file is the most important file. It contains
            all the setting information. Do not modify it without developer's
            instruction
            - You can have photos from your local source or from url. If the photo
            is from URL please copy its path and paste in the corresponding box.
            If the photo is stored locally, it is advised to use the integrated file
            browser to choose the file.
            
        '''
        msg.setDetailedText(instruction)
        msg.exec_()
    def openSettings(self):
        self.settingsSetup.show()    
        self.settingsSetup.emittedLannister.connect(self.loadSettings)
        self.setImageBlur()
    def keyPressEvent(self, event):
        if type(event) == QtGui.QKeyEvent:
            mormont=event.key()
            if(mormont==self.key1):
                self.button1.setStyleSheet('QLabel { color: rgb(0, 185, 255); }')
                self.setUnblur(self.pic1)
            elif(mormont==self.key2):
                self.button2.setStyleSheet('QLabel { color: rgb(0, 185, 255); }')
                self.setUnblur(self.pic2)
            elif(mormont==self.key3):
                self.button3.setStyleSheet('QLabel { color: rgb(0, 185, 255); }')
                self.setUnblur(self.pic3)
            elif(mormont==self.key4):
                self.button4.setStyleSheet('QLabel { color: rgb(0, 185, 255); }')
                self.setUnblur(self.pic4)
            elif(mormont==self.key5):
                self.button5.setStyleSheet('QLabel { color: rgb(0, 185, 255); }')
                self.setUnblur(self.pic5)
                        
            # if event.key() == Qt.Key_1:
            #     self.setUnblur(self.pic1)
            #     #self.emit(QtCore.SIGNAL('MYSIGNAL'))
    def keyReleaseEvent(self, event):
        if type(event) == QtGui.QKeyEvent:
            mormont=event.key()
            
            if(mormont==self.key1):
                self.button1.setStyleSheet('QLabel { color: rgb(255, 255, 255); }')                
                self.setImageBlur()
            elif(mormont==self.key2):
                self.button2.setStyleSheet('QLabel { color: rgb(255, 255, 255); }')
                self.setImageBlur()
            elif(mormont==self.key3):
                self.button3.setStyleSheet('QLabel { color: rgb(255, 255, 255); }')
                self.setImageBlur()
            elif(mormont==self.key4):
                self.button4.setStyleSheet('QLabel { color: rgb(255, 255, 255); }')
                self.setImageBlur()
            elif(mormont==self.key5):
                self.button5.setStyleSheet('QLabel { color: rgb(255, 255, 255); }')
                self.setImageBlur()
    def loadImage(self,path,imgNo):
        basewidth=199
        img = Image.open(os.path.abspath(path))
        wpercent = (basewidth/float(img.size[0]))
        hsize = int((float(img.size[1])*float(wpercent)))
        img = img.resize((basewidth,hsize), Image.ANTIALIAS)
        if(path.lower().endswith('.jpg')):
            img.save(os.path.abspath(os.getcwd()+'/tmp/'+imgNo+'.jpg'))
            img1=QPixmap(os.path.abspath(os.getcwd()+'/tmp/'+imgNo+'.jpg'))
        elif(path.lower().endswith('.png')):
            img.save(os.path.abspath(os.getcwd()+'/tmp/'+imgNo+'.png'))
            img1=QPixmap(os.path.abspath(os.getcwd()+'/tmp/'+imgNo+'.png'))
        return img1
    def setUnblur(self,pic):
        romoEtan=QGraphicsBlurEffect()
        romoEtan.setBlurRadius(0.0)
        pic.setGraphicsEffect(romoEtan)  
    def setImageBlur(self):
        romoEtan=QGraphicsBlurEffect()
        romoEtan.setBlurRadius(20.0)
        self.pic1.setGraphicsEffect(romoEtan)
        romoEtan=QGraphicsBlurEffect()
        romoEtan.setBlurRadius(20.0)
        self.pic2.setGraphicsEffect(romoEtan)
        romoEtan=QGraphicsBlurEffect()
        romoEtan.setBlurRadius(20.0)
        self.pic3.setGraphicsEffect(romoEtan)
        romoEtan=QGraphicsBlurEffect()
        romoEtan.setBlurRadius(20.0)
        self.pic4.setGraphicsEffect(romoEtan)
        romoEtan=QGraphicsBlurEffect()
        romoEtan.setBlurRadius(20.0)
        self.pic5.setGraphicsEffect(romoEtan)
    
    def loadSettings(self):
        if not (os.path.exists('settings.dc')):
            return
        inpFile=open('settings.dc','r')
        conInp=inpFile.readlines()
        inpFile.close()

        path1=conInp[0][0:len(conInp[0])-1]
        path2=conInp[1][0:len(conInp[1])-1]
        path3=conInp[2][0:len(conInp[2])-1]
        path4=conInp[3][0:len(conInp[3])-1]
        path5=conInp[4][0:len(conInp[4])-1]
        
        
        if(path1=='-'):
            pass
        elif(validators.url(path1)):
            f=open('temp.jpg','wb')
            f.write(urllib.request.urlopen(path1).read())
            f.close()
            img1=self.loadImage('temp.jpg','1')
            self.pic1.setPixmap(img1)
            os.remove('temp.jpg')
        else:
            img1=self.loadImage(path1,'1')
            self.pic1.setPixmap(img1)
        
        if(path2=='-'):
            pass
        elif(validators.url(path2)):
            f=open('temp.jpg','wb')
            f.write(urllib.request.urlopen(path2).read())
            f.close()
            img2=self.loadImage('temp.jpg','2')
            self.pic2.setPixmap(img2)
            os.remove('temp.jpg')
        else:
            img2=self.loadImage(path2,'2')
            self.pic2.setPixmap(img2)
        
        if(path3=='-'):
            pass
        elif(validators.url(path3)):
            f=open('temp.jpg','wb')
            f.write(urllib.request.urlopen(path3).read())
            f.close()
            img3=self.loadImage('temp.jpg','3')
            self.pic3.setPixmap(img3)
            os.remove('temp.jpg')
        else:
            img3=self.loadImage(path3,'3')
            self.pic3.setPixmap(img3)
        
        if(path4=='-'):
            pass
        elif(validators.url(path4)):
            f=open('temp.jpg','wb')
            f.write(urllib.request.urlopen(path4).read())
            f.close()
            img4=self.loadImage('temp.jpg','4')
            self.pic4.setPixmap(img4)
            os.remove('temp.jpg')
        else:
            img4=self.loadImage(path4,'4')
            self.pic4.setPixmap(img4) 
        
        if(path5=='-'):
            pass
        elif(validators.url(path5)):
            f=open('temp.jpg','wb')
            f.write(urllib.request.urlopen(path5).read())
            f.close()
            img5=self.loadImage('temp.jpg','5')
            self.pic5.setPixmap(img5)
            os.remove('temp.jpg')
        else:
            img5=self.loadImage(path5,'5')
            self.pic5.setPixmap(img5)       
        
        #button text
        # self.button1.setText(conInp[5][0:len(conInp[5])-1])
        # self.button2.setText(conInp[6][0:len(conInp[6])-1])
        # self.button3.setText(conInp[7][0:len(conInp[7])-1])
        # self.button4.setText(conInp[8][0:len(conInp[8])-1])
        # self.button5.setText(conInp[9][0:len(conInp[9])-1])
        self.populateButtonName(path1,self.button1)
        self.populateButtonName(path2,self.button2)
        self.populateButtonName(path3,self.button3)
        self.populateButtonName(path4,self.button4)
        self.populateButtonName(path5,self.button5)


        self.key1=self.keyValStore(conInp[5][0:len(conInp[5])-1])
        self.key2=self.keyValStore(conInp[6][0:len(conInp[6])-1])
        self.key3=self.keyValStore(conInp[7][0:len(conInp[7])-1])
        self.key4=self.keyValStore(conInp[8][0:len(conInp[8])-1])
        self.key5=self.keyValStore(conInp[9][0:len(conInp[9])-1])

        # self.key1=ord(conInp[5][0:len(conInp[5])-1])
        # self.key2=ord(conInp[6][0:len(conInp[6])-1])
        # self.key3=ord(conInp[7][0:len(conInp[7])-1])
        # self.key4=ord(conInp[8][0:len(conInp[8])-1])
        # self.key5=ord(conInp[9][0:len(conInp[9])-1])
    def populateButtonName(self,name,butt):
        if(name=='-'):
            pass
        elif(validators.url(name)):
            print(name)
            name=name[name.rfind('/')+1:len(name)]
            name=name[0:name.rfind('.')]
            butt.setText(name)
            
        else:
            #name=os.path.abspath(name)
            name=name[name.rfind('/')+1:len(name)]
            name=name[0:name.rfind('.')]
            butt.setText(name)
            
    
    def keyValStore(self,key):
        if(key.isnumeric()==True):
            return ord(key)
        else:
            key=key.lower()
            return ord(key)-32
    def setBlur(self):
        pass
def main():
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    settingsGui=settings.Settings()
    form = PhotoSelector(settingsGui)                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app
if __name__=='__main__':
    main()