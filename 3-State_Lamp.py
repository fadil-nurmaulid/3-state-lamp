#Three State Lamp

import sys, os
from PyQt5.QtWidgets import (QApplication, QWidget,
                             QHBoxLayout, QPushButton)
from PyQt5.QtGui import QIcon, QFont, QFontDatabase

class Lamp(QWidget):
    def __init__(self):
        super().__init__()
        self.button = QPushButton("0", self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle("3-State Lamp")
        icon_path = os.path.join(os.path.dirname(__file__), "assets/Icon.jpg")
        self.setWindowIcon(QIcon(icon_path))
        self.setGeometry(500, 175, 400, 210)
        self.setFixedSize(400, 210)
        self.setStyleSheet("background-color: rgb(60, 182, 191)")

        font_path = os.path.join(os.path.dirname(__file__), "assets/DS-DIGIT.TTF")
        font_id = QFontDatabase.addApplicationFont(font_path)
        font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(font_family)
        self.button.setFont(my_font)

        hbox = QHBoxLayout()
        hbox.addWidget(self.button)

        self.setLayout(hbox)

        self.button.setStyleSheet("font-size: 180px;"
                                  "background-color: gray;")

        self.lamp_state = [0, 1, 2]
        self.current_state = 1
        
        self.button.clicked.connect(self.toggle)

    def toggle(self):
        self.button.setText(str(self.lamp_state[self.current_state]))
        
        match self.lamp_state[self.current_state]:
            case 0:
                self.button.setStyleSheet("font-size: 180px;"
                                          "background-color: gray;")
            case 1:
                self.button.setStyleSheet("font-size: 180px;"
                                          "background-color: rgb(192, 192, 64);")    
            case 2:
                self.button.setStyleSheet("font-size: 180px;"
                                          "background-color: yellow;")
        
        self.current_state = (self.current_state + 1) % 3

if __name__ == '__main__':
    app = QApplication(sys.argv)
    lamp_app = Lamp()
    lamp_app.show()
    sys.exit(app.exec_())
    