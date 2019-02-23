from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon, QPixmap
from gomoku.newQLabel import QLabel_new
from PyQt5.QtWidgets import QWidget
from gomoku.GUI import GUI
import numpy as np
import re
import sys


class Main:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        ex = GUI()
        ex.show()
        sys.exit(app.exec_())



if __name__ == '__main__':
    main = Main()
