#sys
import sys

#Importing the components we need
from PySide6.QtWidgets import QApplication,QMainWindow, QPushButton

class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Button Holder app")
        button = QPushButton("Press Me!")

        self.setCentralWidget(button)


app = QApplication(sys.argv)

window = ButtonHolder()
window.show()

#Start the event loop
app.exec()