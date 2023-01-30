from PySide6.QtWidgets import QMainWindow, QPushButton


class ButtonHolder(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First app")   
        button = QPushButton("Press me")
        #set outton as centeral object
        self.setCentralWidget(button)