from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QPainter,QTransform

class ImageLabel(QtWidgets.QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self._image = None
        

    def setImage(self, image):
        self._image = image
        self.update()

    def paintEvent(self, event):
        if self._image is None or self._image.isNull():
            return
        painter = QPainter(self)
        width = self.width()
        height = self.height()
        imageWidth = self._image.width()
        imageHeight = self._image.height()
        r1 = width / imageWidth
        r2 = height / imageHeight
        r = min(r1, r2)
        x = (width - imageWidth * r) / 2
        y = (height - imageHeight * r) / 2
        painter.setTransform(QTransform().translate(x, y).scale(r,r))
        painter.drawImage(QtCore.QPointF(0,0), self._image)
