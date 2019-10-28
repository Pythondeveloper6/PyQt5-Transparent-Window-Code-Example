from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication([])

window = QWidget()
window.setWindowFlags(Qt.FramelessWindowHint)
window.setAttribute(Qt.WA_TranslucentBackground)
window.show()

layout = QVBoxLayout(window)
button = QPushButton('Exit')
button_test = QPushButton('Test')
le = QLineEdit()
button.clicked.connect(app.quit)
layout.addWidget(button)
layout.addWidget(button_test)
layout.addWidget(le)

app.exec_()
