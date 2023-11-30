from PyQt5.QtWidgets import QWidget,QVBoxLayout,QLabel,QSizePolicy
from PyQt5.QtGui import QImage
from PyQt5.QtCore import Qt
from ImageLabel import ImageLabel
import os

class ImageWidget(QWidget):
    def __init__(self,path,parent):
        super().__init__()
        
        
        
        self.path=path
        
        layout = QVBoxLayout(self)

        imgLabel=ImageLabel(self)
        dataLabel=QLabel(self)
        pathLabel=QLabel(self)
        
        pathLabel.mouseReleaseEvent=self.clicked
        pathLabel.setStyleSheet("color: blue") 
        
        img=QImage(path)
        imgLabel.setImage(img)
        
        
        size=img.size()
        height,width=size.height(),size.width()
        
        self.setMinimumWidth(min(800,width))
        dataLabel.setText(f"({height} x {width})")
        pathLabel.setText(path)
        
        imgLabel.setSizePolicy(QSizePolicy.Expanding , QSizePolicy.Expanding)
        

        
        dataLabel.setAlignment(Qt.AlignCenter)
        pathLabel.setAlignment(Qt.AlignCenter)
        
        layout.addWidget(imgLabel)
        layout.addWidget(dataLabel)
        layout.addWidget(pathLabel)
        

        
        self.setLayout(layout)
        self.show()
    
    
    def clicked(self,_):
        os.startfile(self.path)
        
        