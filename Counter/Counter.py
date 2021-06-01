from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import counter_ui as ui

class Main(QMainWindow, ui.Ui_MainWindow):
    

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.Button_1.clicked.connect(lambda: self.addNumber('1'))
        self.Button_2.clicked.connect(lambda: self.addNumber('2'))
        self.Button_3.clicked.connect(lambda: self.addNumber('3'))
        self.Button_4.clicked.connect(lambda: self.addNumber('4'))
        self.Button_5.clicked.connect(lambda: self.addNumber('5'))
        self.Button_6.clicked.connect(lambda: self.addNumber('6'))
        self.Button_7.clicked.connect(lambda: self.addNumber('7'))
        self.Button_8.clicked.connect(lambda: self.addNumber('8'))
        self.Button_9.clicked.connect(lambda: self.addNumber('9'))
        self.Button_0.clicked.connect(lambda: self.addNumber('0'))
        self.Button_doc.clicked.connect(lambda: self.addNumber('.'))
        self.Button_plus.clicked.connect(lambda : self.addNumber('+'))
        self.Button_minus.clicked.connect(lambda : self.addNumber('-'))
        self.Button_muti.clicked.connect(lambda : self.addNumber('*'))
        self.Button_div.clicked.connect(lambda : self.addNumber('/'))
        self.Button_C.clicked.connect(self.cleaneq)



        self.Button_total.clicked.connect(self.eqcount)

    def addNumber(self, number):
        self.lineEdit.insert(number)

    def eqcount(self):
        eq = self.lineEdit.text()
        value = eval(eq)
        self.lineEdit.setText(str(value))
        print(value)
    def cleaneq(self):
        self.lineEdit.setText('')



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    Eq = ''


    sys.exit(app.exec_())










