from PySide6.QtWidgets import QMainWindow, QToolBar, QPushButton, QStatusBar
from PySide6.QtGui import QAction, QIcon

from PySide6.QtCore import QSize

class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app  #declare an app member
        self.setWindowTitle("CustomWindow")


        #menubar and menu
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("&File")
        quit_action =file_menu.addAction("Quit")
        quit_action.triggered.connect(self.quit_app)

        edit_menu = menu_bar.addMenu("Edit")
        quit_action =edit_menu.addAction("Copy")
        quit_action =edit_menu.addAction("Cut")
        quit_action =edit_menu.addAction("Paste")
        quit_action =edit_menu.addAction("Undo")
        quit_action =edit_menu.addAction("Redo")

        #A bunch of other menu options
        menu_bar.addMenu("Window")
        menu_bar.addMenu("Setting")
        menu_bar.addMenu("Help")


        #Working with toolbar
        toolbar = QToolBar(" My main toolbar ")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        #Add the quit action to the toolbar
        toolbar.addAction(quit_action)


        action1 = QAction('Some Action', self)
        action1.setStatusTip('Status message for some  action')
        action1.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action1)


        action2 = QAction(QIcon('start.png'), 'Some Action', self)
        action2.setStatusTip('Status message for some action')  #show when u hover over it
        action2.triggered.connect(self.toolbar_button_click)
        toolbar.addAction(action2)

        toolbar.addSeparator()
        toolbar.addWidget(QPushButton("Click here"))

        #Working with status bar
        self.setStatusBar(QStatusBar(self))


        button1 =QPushButton("Button1")
        button1.clicked.connect(self.button1_clicked)
        self.setCentralWidget(button1)


    def button1_clicked(self):
        print('Clicked on the button')


    def quit_app(self):
        self.app.quit()

    def toolbar_button_click(self):
        self.statusBar().showMessage("Message from my app", 3000)


