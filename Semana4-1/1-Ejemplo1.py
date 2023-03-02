from PyQt5.QtWidgets import QWidget, QApplication

application = QApplication([])
mainWindow = QWidget()

mainWindow.setGeometry(0,0,1280,720)
mainWindow.setWindowTitle('Hola mundo')

mainWindow.show()
application.exec()