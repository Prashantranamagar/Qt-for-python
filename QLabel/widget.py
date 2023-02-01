    from PySide6.QtGui import QPixmap
    from PySide6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout 


    class Widget(QWidget):
        def  __init__(self):
            super().__init__()

            self.setWindowTitle("QLabel Image Demo")
            image_label =QLabel()
            image_label.setPixmap(QPixmap("images/abc.jpg"))

            layout =QVBoxLayout()
            layout.addWidget(image_label)

            self.setLayout(layout)


