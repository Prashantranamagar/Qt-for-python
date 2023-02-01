from PySide6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QWidget, QSizePolicy, QGridLayout



class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Size policies and stretches")


        btn_1 = QPushButton("btn_1")
        btn_2 = QPushButton("btn_2")
        btn_3 = QPushButton("btn_3")
        btn_3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        btn_4 = QPushButton("btn_4")
        btn_5 = QPushButton("btn_5")
        btn_6 = QPushButton("btn_6")
        btn_7 = QPushButton("btn_7")

        #Grid layout
        grid_layout =QGridLayout()
        grid_layout.addWidget(btn_1, 0,0)  #at index 0,0 of the 
        grid_layout.addWidget(btn_2, 0,1,1,2) #at index (0,1) Take 1 row and 2 column
        grid_layout.addWidget(btn_3, 1,0,2,1)  #At index (1,0) Take 2row and 1 column
        grid_layout.addWidget(btn_4, 1,1)
        grid_layout.addWidget(btn_5, 1,2)
        grid_layout.addWidget(btn_6, 2,1)
        grid_layout.addWidget(btn_7, 2,2)

        self.setLayout(grid_layout)
 



        
        