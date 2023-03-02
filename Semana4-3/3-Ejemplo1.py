from PyQt5.QtWidgets import QMainWindow, QApplication, QAction

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle('Dropdown Menu')
        self.setGeometry(0,0,350,400)
        self.addMenu()
        
    def addMenu(self):
        menuBar = self.menuBar()
        
        fileMenu = menuBar.addMenu('File')
        helpMenu = menuBar.addMenu('Help')
        
        visitWebsiteAction = QAction('Visit Our Website',self)
        fileBugReportAction = QAction('File a Bug Report',self)
        
        helpMenu.addAction(visitWebsiteAction)
        helpMenu.addAction(fileBugReportAction)
        
        followUs = helpMenu.addMenu('Follow Us')
        
        twitterAction = QAction('Twitter',self)
        githubAction = QAction('GitHub',self)
        
        followUs.addAction(twitterAction)
        followUs.addAction(githubAction)
        
if(__name__=='__main__'):
    application = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    application.exec()