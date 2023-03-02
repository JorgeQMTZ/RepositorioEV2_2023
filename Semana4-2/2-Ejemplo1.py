import sys

from PyQt5.QtWidgets import QWidget, QApplication, QCheckBox, QLineEdit, QLabel, QSlider, QLCDNumber, QCalendarWidget, QGroupBox, QRadioButton, QVBoxLayout
from PyQt5.QtCore import Qt


class Example(QWidget):
    def __init__ (self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.addCheckBox()
        self.addLineEdit()
        self.addSlider()
        self.addCalendar()
        self.addRadioBoton()

        self.resize(640, 320)
        self.setWindowTitle('Controles PyQT 5 by Tutor de Programacion')

    def addRadioBoton(self):
        gbx = QGroupBox('Tu Lenguaje Favorito', self)
        gbx.setGeometry(20, 150, 185, 120)
        radio1 = QRadioButton("C/C++")
        radio2 = QRadioButton("Python")
        radio3 = QRadioButton("Java")
        vbox = QVBoxLayout(self)
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        gbx.setLayout(vbox)
        radio1.setChecked(True)
        print(radio1.isChecked())

    def addCalendar(self):
        cal=QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked.connect(self.timeSelected)
        cal.move(300, 20)

    def timeSelected(self, date):
        print('La Fecha es: ', date.toString())

    def addSlider(self):
        sld = QSlider(Qt.Horizontal, self)
        sld.setGeometry(20, 80, 150, 30)
        sld.setRange(50, 250)
        sld.setValue(120)
        sld.valueChanged.connect(self.valChange)
    
        num = QLCDNumber(self)
        num.setGeometry(180, 80, 50, 30)
        num.display(sld.value())
        sld.valueChanged.connect(num.display)

    def valChange(self, value):
        print('QSlider value: ', value)

    def addLineEdit(self):
        lbl = QLabel('Nombre:', self)
        lbl.move(20, 52)
        txt = QLineEdit(self)
        txt.move(72, 50)
        txt.setPlaceholderText('Dime tu nombre')
        txt.textChanged.connect(self.textChange)
        txt.setFocus()
        nombre = txt.text()

    def textChange(self, text):
        print('El nuevo texto es: ', text)
    def addCheckBox(self):
        cbx = QCheckBox('Mostrar/Ocultar', self)
        cbx.setCheckState(Qt.PartiallyChecked)
        cbx.stateChanged.connect(self.cbxChange)
        cbx.move(20, 20)

    def cbxChange(self, state):
        print('CheckBox State: ', state)


if __name__=='__main__':
    app = QApplication(sys.argv)
    win = Example()
    win.show()
    sys.exit(app.exec_())