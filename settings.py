import urllib.request #to get url request
from PyQt5 import QtGui, QtWidgets, QtCore # Import the PyQt5 module we'll need
from PyQt5.QtWidgets import QApplication, QMessageBox, QWidget, QInputDialog, QLineEdit, QFileDialog,QTableWidget, QTableWidgetItem
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication, QUrl, QDate
import sys # We need sys so that we can pass argv to QApplication
import os
import settingDesign

def getFileName(extension='(.*)'):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    #extension='Files '+extension
    fileName,_= QFileDialog.getOpenFileName(caption='Select file',filter=extension)
    if(fileName):
        return fileName
class Settings(QtWidgets.QMainWindow, settingDesign.Ui_MainWindow):
    emittedLannister=QtCore.pyqtSignal()
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in design.py file automatically
                            # It sets up layout and widgets that are defined
        # self.path1.setText('-')
        # self.path2.setText('-')
        # self.path3.setText('-')
        # self.path4.setText('-')
        # self.path5.setText('-')
        # self.key1.setText('-')
        # self.key2.setText('-')
        # self.key3.setText('-')
        # self.key4.setText('-')
        # self.key5.setText('-')
        self.readSettingFile()
        self.fileButton1.clicked.connect(self.pathFile1)
        self.fileButton2.clicked.connect(self.pathFile2)
        self.fileButton3.clicked.connect(self.pathFile3)
        self.fileButton4.clicked.connect(self.pathFile4)
        self.fileButton5.clicked.connect(self.pathFile5)

        self.key1.textChanged[str].connect(self.onChangedKey1)
        self.key2.textChanged[str].connect(self.onChangedKey2)
        self.key3.textChanged[str].connect(self.onChangedKey3)
        self.key4.textChanged[str].connect(self.onChangedKey4)
        self.key5.textChanged[str].connect(self.onChangedKey5)

        self.saveButton.clicked.connect(self.saveSettings)
        self.clearButton.clicked.connect(self.clearAll)
    
    def clearAll(self):
        self.path1.setText('-')
        self.path2.setText('-')
        self.path3.setText('-')
        self.path4.setText('-')
        self.path5.setText('-')

        self.key1.setText('-')
        self.key2.setText('-')
        self.key3.setText('-')
        self.key4.setText('-')
        self.key5.setText('-')

    def readSettingFile(self):
        inpFile=open('settings.dc')
        conInp=inpFile.readlines()
        inpFile.close()

        self.path1.setText(conInp[0][0:len(conInp[0])-1])
        self.path2.setText(conInp[1][0:len(conInp[1])-1])
        self.path3.setText(conInp[2][0:len(conInp[2])-1])
        self.path4.setText(conInp[3][0:len(conInp[3])-1])
        self.path5.setText(conInp[4][0:len(conInp[4])-1])

        self.key1.setText(conInp[5][0:len(conInp[5])-1])
        self.key2.setText(conInp[6][0:len(conInp[6])-1])
        self.key3.setText(conInp[7][0:len(conInp[7])-1])
        self.key4.setText(conInp[8][0:len(conInp[8])-1])
        self.key5.setText(conInp[9][0:len(conInp[9])-1])

    def onChangedKey1(self,text):
        if(len(text)>1):
            self.key1.setText(self.key1.text()[0:len(self.key1.text())-1])
    def onChangedKey2(self,text):
        if(len(text)>1):
            self.key2.setText(self.key2.text()[0:len(self.key2.text())-1])
    def onChangedKey3(self,text):
        if(len(text)>1):
            self.key3.setText(self.key3.text()[0:len(self.key3.text())-1])
    def onChangedKey4(self,text):
        if(len(text)>1):
            self.key4.setText(self.key4.text()[0:len(self.key4.text())-1])
    def onChangedKey5(self,text):
        if(len(text)>1):
            self.key5.setText(self.key5.text()[0:len(self.key5.text())-1])
    def saveSettings(self):
        if not (os.path.exists('tmp')):
            os.mkdir('tmp',mode=0o777)
        with open('settings.dc','w+') as setWriter:
            setWriter.write(self.path1.text()+'\n')
            setWriter.write(self.path2.text()+'\n')
            setWriter.write(self.path3.text()+'\n')
            setWriter.write(self.path4.text()+'\n')
            setWriter.write(self.path5.text()+'\n')
            setWriter.write(self.key1.text()+'\n')
            setWriter.write(self.key2.text()+'\n')
            setWriter.write(self.key3.text()+'\n')
            setWriter.write(self.key4.text()+'\n')
            setWriter.write(self.key5.text()+'\n')
        if not(self.signalsBlocked()):
            self.emittedLannister.emit()
            self.close()
            
    def pathFile1(self):
        #self.path1.setText(getFileName('JPEG File (*.jpg);;PNG File(*.png);;All files(*.*)'))
        self.path1.setText(getFileName('JPEG File (*.jpg);;PNG File(*.png)'))
    def pathFile2(self):
        self.path2.setText(getFileName('JPEG File (*.jpg);;PNG File(*.png)'))
    def pathFile3(self):
        self.path3.setText(getFileName('JPEG File (*.jpg);;PNG File(*.png)'))
    def pathFile4(self):
        self.path4.setText(getFileName('JPEG File (*.jpg);;PNG File(*.png)'))
    def pathFile5(self):
        self.path5.setText(getFileName('JPEG File (*.jpg);;PNG File(*.png)'))
    

def main():
    app = QtWidgets.QApplication(sys.argv)  # A new instance of QApplication
    form = Settings()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
    app.exec_()                         # and execute the app
if __name__=='__main__':
    main()