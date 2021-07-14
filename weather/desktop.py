import sys
from PyQt6.QtWidgets import QMainWindow, QApplication
from PyQt6.QtGui import QIcon
from PyQt6 import QtCore


class MyWin(QMainWindow):
    def __init__(self, parent=None):
        super(MyWin, self).__init__(parent)
        self.setGeometry(250, 350, 250, 300)
        self.setWindowTitle("My Windows")
        self.setWindowIcon(QIcon('done.jpg'))
        self.show()


def main(args):
    app = QApplication([])

    ww = MyWin()
    sys.exit(app.exec())


if __name__ == '__main__':
    main(sys.argv)
