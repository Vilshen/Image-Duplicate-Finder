from PyQt5.QtWidgets import QWidget,QListView,QVBoxLayout
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtCore import QModelIndex


class ClusterList(QWidget):
    def __init__(self,parent):
        super(QWidget, self).__init__()
        
        self.parent=parent
            
        mainlayout = QVBoxLayout()
        self.setLayout(mainlayout)
            
        self.listView = QListView()
        self.model = QStandardItemModel()
        self.listView.setModel(self.model)
        
        mainlayout.addWidget(self.listView)
        
        self.listView.clicked[QModelIndex].connect(self.on_clicked)
        
    def on_clicked(self, index):
        self.parent.parent.switchImages(self.model.itemFromIndex(index).text())