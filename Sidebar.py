from PyQt5.QtWidgets import QWidget,QVBoxLayout

from ClusterList import ClusterList
from ControlPanel import ControlPanel

class Sidebar(QWidget):
    def __init__(self,parent):
        super(Sidebar, self).__init__()
        
        self.parent=parent
        
        self.setMaximumWidth(500)
        
        widget = QWidget()
        layout = QVBoxLayout(widget)
        
        self.clusList=ClusterList(self)
        layout.addWidget(self.clusList)
        layout.addWidget(ControlPanel(self))
        
        
        
        self.setLayout(layout)
        
        self.show()