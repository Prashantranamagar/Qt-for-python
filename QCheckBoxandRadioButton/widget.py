from PySide6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QSizePolicy, QGridLayout, QGroupBox, QCheckBox, QButtonGroup, QRadioButton



class Widget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Size policies and stretches")


        #Checkboxes : operating system
        os = QGroupBox("Choose operating systems")

        windows =QCheckBox("Windows")
        windows.toggled.connect(self.windows_box_toggeled)

        linux = QCheckBox("linux")
        linux.toggled.connect(self.linux_box_toggeled)

        mac = QCheckBox("linux")
        mac.toggled.connect(self.mac_box_toggeled)

        #Checkboxes: Os layout    
        os_layout = QVBoxLayout()
        os_layout.addWidget(windows)
        os_layout.addWidget(linux)
        os_layout.addWidget(mac)
        os.setLayout(os_layout)


        #Checkboxes: drinks
        drinks =QGroupBox('Choose your drink')
        beer =QCheckBox("Beer")
        juice =QCheckBox("Juice")
        coffe =QCheckBox("Coffe")
        # beer.setChecked(True)  #checked beer from the start


        #Exclusive checkboxes --> exclusive (can only choose one checkbox)
        #Make the checkboxes exclusive
        exclusive_button_group = QButtonGroup(self)  # The self parent is needed here.
        exclusive_button_group.addButton(beer)
        exclusive_button_group.addButton(juice)
        exclusive_button_group.addButton(coffe)

        #Checkboxes: Drinks layout
        drinks_layout = QVBoxLayout()
        drinks_layout.addWidget(beer)
        drinks_layout.addWidget(juice)
        drinks_layout.addWidget(coffe)
        drinks.setLayout(drinks_layout)


        #Radio button: answers 
        answers = QGroupBox('Choose your answers')
        ans_a = QRadioButton('A')
        ans_a.setChecked(True)
        ans_b = QRadioButton('B')
        ans_c = QRadioButton('C')

        #Radio buttons : answers layout
        answers_layout =QVBoxLayout()
        answers_layout.addWidget(ans_a)
        answers_layout.addWidget(ans_b)
        answers_layout.addWidget(ans_c)
        answers.setLayout(answers_layout)


        layout =QVBoxLayout()
        layout.addWidget(os)
        layout.addWidget(drinks)
        layout.addWidget(answers)


        self.setLayout(layout)

    def windows_box_toggeled(self, checked):
        if(checked):
            print('Window box is checked')
        else:
            print('Window box unckecked')

    def linux_box_toggeled(self, checked):
        if(checked):
            print('Linux box is checked')
        else:
            print('Linux box unckecked')
    
    def mac_box_toggeled(self, checked):
        if(checked):
            print('Mac box is checked')
        else:
            print('Mac box unckecked')
