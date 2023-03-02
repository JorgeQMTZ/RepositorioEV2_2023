from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import (
    QLabel,
    QWidget,
    QApplication,
    QHBoxLayout,
)

application = QApplication([])

mainWindow = QWidget()
mainWindow.setGeometry(0,0,1280,720)
mainWindow.setWindowTitle('Geometry Dash')

horizontalLayout = QHBoxLayout()

for num in range(4):
    label = QLabel()
    pixmap = QPixmap('icon_37.png')
    label.setPixmap(pixmap)
    horizontalLayout.addWidget(label)
    
mainWindow.setLayout(horizontalLayout) 
mainWindow.show()
application.exec()