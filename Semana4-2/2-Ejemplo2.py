import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QComboBox, QStyleFactory, QListWidget, QTableWidget, QTableWidgetItem, QListWidgetItem


class Example(QWidget):
    def __init__ (self, parent=None):
        super(Example, self).__init__ (parent)
        QApplication.setStyle(QStyleFactory.create('Fusion'))

        cbx = QComboBox()
        cbx.addItems(QStyleFactory.keys())
        cbx.currentTextChanged.connect(self.textChanged)
        cbx.setItemText(4, 'Fusion')

        items = ['Ubuntu', 'Linux', 'Mac OS', 'Windows', 'Fedora', 'Chrome OS', 'Android', 'Windows Phone']

        self.lv = QListWidget()
        self.lv.addItems(items)
        self.lv.itemSelectionChanged.connect(self.itemChanged)


        self.table = QTableWidget(10, 3)
        self.table.setHorizontalHeaderLabels(['Nombre', 'Edad', 'Nacionalidad']) # evento producido cuando cambia el elemento seleccionado
        self.table.itemSelectionChanged.connect(self.tableItemChanged)
        self.table.setAlternatingRowColors(True)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)

        table_data = [
            ("Alice", 15, "Panama"),
            ("Dana", 25, "Chile"),
            ("Fernada", 18, "Ecuador")
        ]

        for i, (name, age, city) in enumerate(table_data):
            self.table.setItem(i, 0, QTableWidgetItem(name))
            self.table.setItem(i, 1, QTableWidgetItem(str(age)))
            self.table.setItem(i, 2, QTableWidgetItem(city))

        vbx = QVBoxLayout()
        vbx.addWidget(QPushButton('Tutoriales PyQT-5'))
        vbx.setAlignment(Qt.AlignTop)
        vbx.addWidget(cbx)
        vbx.addWidget(self.lv)
        vbx.addWidget(self.table)

        self.setWindowTitle("Items View")
        self.resize(362, 320)
        self.setLayout(vbx)

    def textChanged(self, txt):
        QApplication.setStyle(QStyleFactory.create(txt))

    def itemChanged(self):
        item = QListWidgetItem(self.lv.currentItem())
        print("Sistema seleccionado: ", item.text())

    def tableItemChanged(self):
        name, age, city = self.table.selectedItems()
        print("Data:", name.text(), age.text(), city.text())
 


if __name__== '__main__':
    app = QApplication(sys.argv)
    ejm = Example()
    ejm.show()
    sys.exit(app.exec_())