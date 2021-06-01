from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import cv2
import ImgProcess_ui as ui


class Main(QMainWindow, ui.Ui_MainWindow):
    

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.OpenSoucePath.clicked.connect(self.openfile) #選取圖片來源路徑
        self.OpenSavePath.clicked.connect(self.savefile) #選取圖片儲存路徑
        self.startbt.clicked.connect(self.savestart) #進行勾選圖片處裡選項並輸出

    def openfile(self):
        OpenFilePath, filetype = QFileDialog.getOpenFileName(self,
                      "選取檔案",
                      "./",
                      "All Files (*);;Text Files (*.jpg)")  #設定副檔名過濾,注意用雙分號間隔

        self.SrcPathText.setText(str(OpenFilePath))


    def savefile(self):
        SaveFilePath, ok2 = QFileDialog.getSaveFileName(self,
                  "檔案儲存",
                  "./",
                  "All Files (*);;Text Files (*.txt)")

        self.SavePathText.setText(str(SaveFilePath))
        
    def statecheck(self):
        if self.cbGray.checkState() == Qt.Checked:
            img = self.gray()
            return img
        else:
            pass

    def gray(self):
        image_path = self.SrcPathText.text()
        img = cv2.imread(image_path, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        return img
 
    def savestart(self):
        img = self.statecheck()
        save_path = self.SavePathText.text()    
        cv2.imwrite(save_path,cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    window.show()
    sys.exit(app.exec_())










