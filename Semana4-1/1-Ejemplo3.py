from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

application = QApplication([])

mainWindow = QWidget()
mainWindow.setGeometry(0,0,300,400)
mainWindow.setWindowTitle('Hola mundo')

def clickedSlot():
    print('¿Pa que le picas?')
pushButton = QPushButton(parent = mainWindow, text='Puchale aqui')
pushButton.clicked.connect(clickedSlot)

mainWindow.show()
application.exec()