from PySide6.QtWidgets import QLabel, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QWidget, QSizePolicy



class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Size policies and stretches")

        #Size policy: how the widgets behaves if the container space is expanded     
        label = QLabel("Some text:")
        line_edit = QLineEdit()

        #Settting size policy
                               #setSizePolicy(horizontilly, vertically)             
        line_edit.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)
        label.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Fixed)


        h_layout_1 = QHBoxLayout()
        h_layout_1.addWidget(label)
        h_layout_1.addWidget(line_edit)

        button_1 =QPushButton("One")
        button_2 = QPushButton("Two")
        button_3 =QPushButton("Three")


        #Stretch : how much of the available space (in the layout) is occupied by
        #you specify   the stretch when you add things to layout:
        #button_1 take space 2 unit , button_2 and button_3 each take u 1 unit space

        h_layout_2 =QHBoxLayout()
        h_layout_2.addWidget(button_1,2)
        h_layout_2.addWidget(button_2,1)
        h_layout_2.addWidget(button_3,1)
        

        v_layout =QVBoxLayout()
        v_layout.addLayout(h_layout_1)
        v_layout.addLayout(h_layout_2)

        self.setLayout(v_layout)
