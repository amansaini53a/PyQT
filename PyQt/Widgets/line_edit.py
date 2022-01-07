import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Line Edits")
        self.setGeometry(50,50,350,350)
        self.UI()

    def UI(self):
        self.nameTextBox = QLineEdit(self)
        self.nameTextBox.move(150, 50)
        self.show()


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()