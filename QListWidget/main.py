from PySide6.QtWidgets import QApplication, QWidget
from widget import Widget

import sys

app = QApplication(sys.argv)
window = Widget()
window.show()
app.exec()  