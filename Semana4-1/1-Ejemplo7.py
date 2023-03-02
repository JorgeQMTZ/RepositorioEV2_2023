from PyQt5.QtWidgets import (
    QGroupBox,
    QLabel,
    QLineEdit,
    QPlainTextEdit,
    QRadioButton,
    QSpinBox,
    QVBoxLayout,
    QWidget,
    QApplication,
    QFormLayout,
)

application = QApplication([])

mainWindow = QWidget()
mainWindow.setGeometry(0, 0, 350, 400)
mainWindow.setWindowTitle('Datos Generales')

formLayout = QFormLayout()

nombreLabel = QLabel('Nombre:')
nombreField = QLineEdit()

edadLabel = QLabel('Edad:')
edadField = QSpinBox()
edadField.setMinimum(0)
edadField.setMaximum(130)

genLabel = QLabel('Genero')
genGroup = QGroupBox()
verticalLayout = QVBoxLayout()

for gen in ['Pibe', 'Piba']:
    radioButton = QRadioButton(gen)
    verticalLayout.addWidget(radioButton)

genGroup.setLayout(verticalLayout)

commentLabel = QLabel('Comentarios')
commentField = QPlainTextEdit()

formLayout.addRow(nombreLabel, nombreField)
formLayout.addRow(edadLabel, edadField)
formLayout.addRow(genLabel, genGroup)
formLayout.addRow(commentLabel, commentField)

mainWindow.setLayout(formLayout)
mainWindow.show()
application.exec()