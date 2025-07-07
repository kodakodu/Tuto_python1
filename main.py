#sys
import sys

#Importing the components we need
from PySide6.QtWidgets import QApplication
from components.button_holder import ButtonHolder



app = QApplication(sys.argv)

window = ButtonHolder()
window.show()

#Start the event loop
app.exec()