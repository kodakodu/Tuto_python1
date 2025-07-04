#Importing the components we need
from PySide6.QtWidgets import QApplication,QWidget

#sys
import sys
app = QApplication(sys.argv)

window = QWidget()
window.show()

#Start the event loop
app.exec()