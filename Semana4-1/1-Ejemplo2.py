from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

application = QApplication([])

mainWindow = QWidget()
mainWindow.setGeometry(0,0,300,400)
mainWindow.setWindowTitle('Hola mundo')

pushButton = QPushButton(parent = mainWindow, text='Puchale aqui')

mainWindow.show()
application.exec()