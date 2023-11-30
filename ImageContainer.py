from PyQt5.QtWidgets import QWidget,QScrollArea,QLayout,QHBoxLayout

from ImageWidget import ImageWidget

class ImageContainer(QScrollArea):
    def __init__(self,parent,imgDirs=()):
        super(ImageContainer, self).__init__()
        self.mainWindow=parent
        
        self.widget = QWidget()
        layout = QHBoxLayout(self.widget)
        layout.setSizeConstraint(QLayout.SetMinAndMaxSize)
        
        for img in imgDirs:
            layout.addWidget(ImageWidget(img,self))
        
        self.setWidget(self.widget)
        self.setWidgetResizable(True)
        
        self.show()