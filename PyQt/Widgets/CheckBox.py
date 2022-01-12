import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("CheckBox")
        self.setGeometry(500, 500, 500, 500)
        self.UI()

    def UI(self):
        self.name = QLineEdit(self)
        self.name.setPlaceholderText("Enter Name")
        self.surname = QLineEdit(self)
        self.surname.setPlaceholderText("Enter Surname")
        self.name.move(150,50)
        self.surname.move(150,80)
        self.remember = QCheckBox("Remeneber me", self)
        self.remember.move(150, 110)
        button = QPushButton("Submit", self)
        button.move(200, 140)
        button.clicked.connect(self.submit)

        self.show()

    def submit(self):
        if (self.remember.isChecked()):
            print("Name" + self.name.text() + "Surname" + self.surname.text() + "Remember me is checked")
        else:
            print("Name" + self.name.text() + "Surname" + self.surname.text() + "Remember me is NOT checked")


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())

if __name__ == '__main__':
    main()
