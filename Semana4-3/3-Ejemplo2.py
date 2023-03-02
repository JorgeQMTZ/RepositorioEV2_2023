from PyQt5.QtWidgets import QAction, QApplication, QFormLayout, QGroupBox, QLabel, QPushButton, QVBoxLayout, QWidget, QMainWindow, QLineEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
 

class MainWindow(QMainWindow):
    def __init__ (self, parent=None):
        super().__init__(parent)
        
        self.createUI()
        self.createActions()
        self.creatMenu()
        
    def createUI(self):
        self.setWindowTitle('Password Manager')
        self.resize(800, 500)
        self.setMinimumSize(500, 450)
        
        self._centralWidget = QWidget()
        self._verticalLayout = QVBoxLayout()
        self._centralWidget.setLayout(self._verticalLayout)
        
        self.setCentralWidget(self._centralWidget)
        
        self._verticalLayout.addStretch(1)
        
        self.addLockImage()
        self.addText()
        self.addInputText()
        
        self._verticalLayout.addStretch(1)
        self.addCopyRight()
        
    def addLockImage(self):
        imageLabel = QLabel()
        pixmap = QPixmap('lock.png')
        imageLabel.setPixmap(pixmap)
        
        self._verticalLayout.addWidget(imageLabel, alignment=Qt.AlignCenter)
        
    def addText(self):
        messageLabel = QLabel('Hi there $ . Your vault is locked. Verify your master password to continue.')
        messageLabel.setAlignment(Qt.AlignCenter)
        messageLabel.setFixedWidth(350)
        messageLabel.setMinimumHeight(50)
        messageLabel.setWordWrap(True)
        self._verticalLayout.addWidget(messageLabel, alignment=Qt.AlignCenter)
        
    def addCopyRight(self):
        copyRight = QLabel('Copyright © <a href="https://logrocket.com/">LogRocket</a> 2021')
        copyRight.setOpenExternalLinks(True)
        self._verticalLayout.addWidget(copyRight, alignment=Qt.AlignCenter)
    
    def addInputText(self):
        groupBox = QGroupBox()
        groupBox.setFixedWidth(350)
        
        formLayout = QFormLayout()

        passwordLabel = QLabel('Master Password')
        passwordField = QLineEdit()
        passwordField.setTextMargins(3, 0, 3, 0)
        passwordField.setMinimumWidth(200)
        passwordField.setMaximumWidth(300)
        passwordField.setEchoMode(QLineEdit.Password)
        passwordField.setClearButtonEnabled(True)

        submitLabel = QLabel('Open Your Vault')
        submitField = QPushButton()

        formLayout.addRow(passwordLabel, passwordField)
        formLayout.addRow(submitLabel, submitField)

        groupBox.setLayout(formLayout)
        self._verticalLayout.addWidget(groupBox, alignment=Qt.AlignCenter)
        
    def creatMenu(self):
        menuBar = self.menuBar()
        fileMenu = menuBar.addMenu('File')
        editMenu = menuBar.addMenu('Edit')
        accountMenu = menuBar.addMenu('Account')
        helpMenu = menuBar.addMenu('Help')

        helpMenu.addAction(self.sendEmailAction)
        helpMenu.addAction(self.visitWebsiteAction)
        helpMenu.addAction(self.fileBugReportAction)
        helpMenu.addSeparator()

        followUs = helpMenu.addMenu('Follow Us')
        followUs.addAction(self.twitterAction)
        followUs.addAction(self.facebookAction)
        followUs.addAction(self.githubAction)

    def createActions(self):
        self.sendEmailAction = QAction('Email Us', self)
        self.visitWebsiteAction = QAction('Visit Our Website', self)
        self.fileBugReportAction = QAction('File a Bug Report', self)
        self.twitterAction = QAction('Twitter', self)
        self.facebookAction = QAction('Facebook', self)
        self.githubAction = QAction('GitHub', self)

if (__name__=='__main__'):
    application = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    application.exec()