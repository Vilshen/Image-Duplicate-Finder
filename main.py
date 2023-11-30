import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget,QHBoxLayout
from PyQt5.QtGui import QStandardItem

from ImageContainer import ImageContainer
from Sidebar import Sidebar
from ImageCollector import ImageCollector
from Clustering import Clustering

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        
        self.setWindowTitle("Duplicate finder")

        self.layout = QHBoxLayout()
        
        self.sb=Sidebar(self)
        self.layout.addWidget(self.sb)
        self.layout.addWidget(ImageContainer(self))
        
        widget = QWidget()
        widget.setLayout(self.layout)
        
        
        self.setCentralWidget(widget)
        
        self.RGBmode=False
        self.Threading=False
        
        self.clusters=dict()
    
      
    def switchImages(self,imgKey):
        imgList=self.clusters[imgKey]
        self.layout.removeItem(self.layout.itemAt(1))
        self.layout.addWidget(ImageContainer(self,imgList))
        
    def start(self,searchDir,threshold):
        images=ImageCollector.getImages(searchDir,self.RGBmode,self.Threading)
        clusterGenerator=Clustering(images,self.RGBmode,threshold)
        clusters=clusterGenerator.getClusters()
        self.clusters={v[0]: v for k,v in clusters.items() if len(v)>1}
        clusters=self.clusters
        
        clusterList=self.sb.clusList.model
        clusterList.clear()
        
        for key in self.clusters.keys():
            item=QStandardItem(key)
            clusterList.appendRow(item)
        
        
if __name__ == '__main__':   
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())