# !/usr/bin/env python3

import sys

from modules import calculate_specs
from modules.design import UIMainWindow

from PyQt5 import QtWidgets, QtCore


class MainWindow(QtWidgets.QMainWindow, UIMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
