from PyQt5 import QtCore, QtGui, QtWidgets
from background import *
from mainWindow import Ui_MainWindow
from crypterMot import Ui_Dialog as cryptDialog
from decrypterMot import Ui_Dialog as decryptDialog

import sys

def cryptShow(): #Afficher fenêtre crypterMot
	crypt.show()

def decryptShow(): #Afficher fenêtre decrypterMot
	decrypt.show()

#fonctions associés au bouton su maindow
def crypterMot():
    cryptui.textEdit.clear()
    s=str(cryptui.lineEdit.text())
    cryptui.textEdit.setText(str(crypter(s)))

def decrypterMot():
    decryptui.lineEdit.clear()
    s=decryptui.textEdit.toPlainText()
    decryptui.lineEdit.setText(str(decrypter(int(s))))


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

crypt = QtWidgets.QDialog()
cryptui = cryptDialog()
cryptui.setupUi(crypt)

decrypt = QtWidgets.QDialog()
decryptui = decryptDialog()
decryptui.setupUi(decrypt)

MainWindow.show()

#Associer boutons du menu principal aux fenêtres correspondantes
ui.cryptStr.clicked.connect(cryptShow)
ui.decryptStr.clicked.connect(decryptShow)


#Associer boutons de chaque fenêtre à la fonction correspondante
ui.cryptFile.clicked.connect(decode2code) #mainWindow
ui.decryptFile.clicked.connect(code2decode) #mainWindow
cryptui.pushButton.clicked.connect(crypterMot)
decryptui.pushButton.clicked.connect(decrypterMot)


sys.exit(app.exec_())
