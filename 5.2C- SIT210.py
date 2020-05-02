import sys
from PyQt5.QtWidgets import (QLabel, QRadioButton, QPushButton, QVBoxLayout, QApplication, QWidget)
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setup(10,GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(12,GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(8,GPIO.OUT, initial = GPIO.LOW)


class basicRadiobuttonExample(QWidget):

    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.label = QLabel('Which light do you want to light up')
        self.rbtn1 = QRadioButton('Green')
        self.rbtn2 = QRadioButton('Blue')
        self.rbtn3 = QRadioButton('Red')
        self.label2 = QLabel("")
        
        self.rbtn1.toggled.connect(self.onClicked)
        self.rbtn2.toggled.connect(self.onClicked)
        self.rbtn3.toggled.connect(self.onClicked)
        
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.rbtn1)
        layout.addWidget(self.rbtn2)
        layout.addWidget(self.rbtn3)
        layout.addWidget(self.label2)
        
        self.setGeometry(200, 200, 300, 150)

        self.setLayout(layout)
        self.setWindowTitle('PyQt5 Radio Button Example')

        

        self.show()

    def onClicked(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            if radioBtn.text() == 'Blue':
                print("1")
                GPIO.output(10, GPIO.HIGH)
                GPIO.output(8, GPIO.LOW)
                GPIO.output(12, GPIO.LOW)
            elif radioBtn.text() == 'Green':
                GPIO.output(10, GPIO.LOW)
                GPIO.output(8, GPIO.HIGH)
                GPIO.output(12, GPIO.LOW)
            elif radioBtn.text() == 'Red':
                GPIO.output(10, GPIO.LOW)
                GPIO.output(8, GPIO.LOW)
                GPIO.output(12, GPIO.HIGH)

if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = basicRadiobuttonExample()
    sys.exit(app.exec_())