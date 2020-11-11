import sys

from modules.design import UIMainWindow

from PyQt5 import QtWidgets


class MainWindow(QtWidgets.QMainWindow, UIMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
