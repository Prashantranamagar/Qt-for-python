
#Importing the coponents we need

from PySide6.QtWidgets import QApplication, QLabel, QWidget, QMainWindow, QPushButton

#The sys module is responsible for processing command line arguments.                                                   
import sys

#Version 1

"""
app = QApplication(sys.argv)

window = QMainWindow()
window.setWindowTitle("Our first main window app")
button = QPushButton()
button.setText("Press Me")

window.setCentralWidget(button)

window.show()

#Start the event loop
app.exec()
"""


# Version 2

"""
class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First app")   
        button = QPushButton("Press me")
        #set outton as centeral object
        self.setCentralWidget(button)

app = QApplication(sys.argv)
window = ButtonHolder()
window.show()
app.exec()
"""


# from buttonholder import ButtonHolder
# app = QApplication(sys.argv)
# window = ButtonHolder()
# window.show()
# app.exec()



"""
Signals and slots

"""

# #Version 1: Just responding to the button click: syntax
# from PySide6.QtWidgets import QApplication, QPushButton

# #the slot:respond when something happens
# def button_clicked(data):
#     print("you clicked the button did't you.", data)

# app = QApplication()
# button = QPushButton("Press Me")  #Makes the button checkable,  it is set to false by default.
#                                     #futher clicks  toggle between checked and uncheked states
# button.setCheckable(True)

# #clicked is the signal of QPushbutton. Its emitted when you click on the buttton
# #you can write a slot to the signal using the syntax below:
# button.clicked.connect(button_clicked)
# button.show()
# app.exec()


#Slider

from PySide6.QtWidgets import QApplication, QPushButton, QSlider
from PySide6.QtCore import Qt

#The Slot: Respond when something happens
def respond_to_slider(data):
    print("Slider moved to :", data)


app = QApplication()
slider =QSlider(Qt.Horizontal)
slider.setMinimum(1)
slider.setMaximum(100)
slider.setValue(25)

#you just do the connection the qt system take care of passing the data from signal to slot.
slider.valueChanged.connect(respond_to_slider)
slider.show()
app.exec()


