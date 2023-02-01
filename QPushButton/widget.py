from PySide6.QtWidgets import QWidget, QPushButton, QVBoxLayout , QLabel, QHBoxLayout, QLineEdit

class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Qlabel and QLineEdit')

        #A set of signals we can connect to
        label = QLabel('fullname:')
        self.line_edit = QLineEdit()
        # self.line_edit.textChanged.connect(self.text_changed)
        self.line_edit.cursorPositionChanged.connect(self.curser_position_changed) 
        # self.line_edit.editingFinished.connect(self.editing_finished)  
        # self.line_edit.returnPressed.connect(self.returned_pressed)  
        # self.line_edit.selectionChanged.connect(self.selection_changed)  
        # self.line_edit.textEdited.connect(self.text_edited)  





        

        button = QPushButton("Grab data")
        button.clicked.connect(self.button_clicked)
        self.text_holder_label = QLabel('I am here')

        #Add layout
        h_layout = QHBoxLayout()  #horizontal layout
        h_layout.addWidget(label)
        h_layout.addWidget(self.line_edit)


        #Add layout
        v_layout = QVBoxLayout()  #Vertical layout
        v_layout.addLayout(h_layout)
        v_layout.addWidget(button)
        v_layout.addWidget(self.text_holder_label)


        self.setLayout(v_layout)



    #Slots
    def button_clicked(self):
        # print('Fullname:', self.line_edit.text())
        self.text_holder_label.setText(self.line_edit.text())


    def text_changed(self):
        print('Fullname:', self.line_edit.text())
        self.text_holder_label.setText(self.line_edit.text())

    def curser_position_changed(self, old, new):
        print("Cursor old position:",old, "-new position : ",new)

    def editing_finished(self):
        print('Editing finished')

    def returned_pressed(self):
        print('Returned pressed')

    def selection_changed(self):
        print('Selection changed', self.line_edit.selectedText())

    def selection_changed(self, new_text):
        print('Text edited. New Text', new_text)


