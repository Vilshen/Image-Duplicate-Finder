import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QHBoxLayout

from ImageContainer import ImageContainer

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("Duplicate finder")

        self.layout = QHBoxLayout()
        
        imgDirs=["D:\Downloads\справка_page-0001.jpg","D:\Downloads\img5.jpg","D:\Downloads\FGO_Ending_Final.png"]
        self.layout.addWidget(ImageContainer(self,imgDirs))
        
        widget = QWidget()
        widget.setLayout(self.layout)
        
        
        self.setCentralWidget(widget)
        
        
    
    
       #https://stackoverflow.com/questions/46024724/pyqt-how-to-create-a-scrollable-window
       #https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QListView.html
       #https://stackoverflow.com/questions/56894741/adding-icons-to-items-of-qlistview
        
    #.close() on the ImageContainer to reload it
    #def clicked(self,_):
    #    self.layout.itemAt(0).widget().close()
    #    imgDirs=[r"D:\MEGA\tpm\1596772630815.jpg"]
    #    self.layout.addWidget(ImageContainer(self,imgDirs))

    #with open("mega_dump.json") as theDict:
    #    import json
    #    self.clusters=json.loads(theDict.read())
if __name__ == '__main__':   
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())