from PyQt6.QtCore import *
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *

from view.envego_ui import *
from control.envego_control import *
import sys

class ViewControl(Ui_MainWindow):
    def __init__(self):
        super().__init__()

class MainApp(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

app = QApplication(sys.argv)
mainwindows = MainApp()

def main():
    app = QApplication(sys.argv)
    mainwindows = MainApp()
    widgets = ViewControl()
    widgets.setupUi(mainwindows)

    model_obj = MainFunction(widgets)
    mainwindows.show()
    app.exec()

if __name__ == '__main__':
    main()
