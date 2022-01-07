import sys
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(50,50,350,350)
        self.UI()

    def UI(self):
        self.text = QLabel("Mytext", self)
        enter_button = QPushButton("Enter", self)
        exit_button = QPushButton("Exit",self)
        self.text.move(160,50)
        enter_button.move(100,80)
        exit_button.move(200,80)
        enter_button.clicked.connect(self.enterfunc)
        exit_button.clicked.connect(self.exitfunc)
        self.show()


    def enterfunc(self):
        self.text.setText("Enter")
        self.text.resize(150,20)

    def exitfunc(self):
        self.text.setText("Exit")
        self.text.resize(150, 20)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()