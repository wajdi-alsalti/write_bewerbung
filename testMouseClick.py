from PySide2.QtWidgets import *
import sys
from PySide2 import QtCore

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        # auto complete options                                                 
        names = ["Apple", "Alps","apple", "Berry", "Cherry" ]
        completer = QCompleter(names)

        # create line edit and add auto complete                                
        self.lineedit = QLineEdit()
        self.lineedit2 = QLineEdit()
        self.lineedit.setCompleter(completer)
        self.lineedit.returnPressed.connect(lambda:self.enterPressed())
        self.label = QLabel("label")
        layout.addWidget(self.lineedit, 0, 0)
        layout.addWidget(self.lineedit2, 0, 1)
        layout.addWidget(self.label, 1, 1)
        
        #self.mousePressEvent()
    def enterPressed(self):
        if self.lineedit.text() == "apple":
                self.lineedit2.setText('eat')
        else:
            self.lineedit2.setText('')
    def click(self):
        if self.lineedit.text() == "apple":
                    self.lineedit2.setText('eat')
        else:
            self.lineedit2.setText('')

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton: # left button pressed
                #self.setText ("Click the left mouse button for the event: define it yourself")
                print("Click the left mouse button") # response test statement
                if self.lineedit.text() == "apple":
                    self.lineedit2.setText('eat')
                else:
                    self.lineedit2.setText('')
        elif event.buttons () == QtCore.Qt.RightButton: # right click
                #self.setText ("Click the right mouse button for the event: define it yourself")
                print("right click") # response test statement
        elif event.buttons () == QtCore.Qt.MidButton: #  Press
                #self.setText ("Click the middle mouse button for the event: define it yourself")
                print("click the middle mouse button") # response test statement
        elif event.buttons () == QtCore.Qt.LeftButton | QtCore.Qt.RightButton: # Left and right buttons simultaneously pressed
                #self.setText ("Also click the left and right mouse button event: define it yourself")
                print("Click the left and right mouse button") # response test statement
        elif event.buttons () == QtCore.Qt.LeftButton | QtCore.Qt.MidButton: # Left middle button simultaneously pressed
                #self.setText ("Also click the middle left mouse button event: define it yourself")
                print("Click the left middle button") # response test statement
        elif event.buttons () == QtCore.Qt.MidButton | QtCore.Qt.RightButton: #  
                #self.setText ("Also click the middle right mouse button event: define it yourself")
                print("click the middle right button") # response test statement

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())