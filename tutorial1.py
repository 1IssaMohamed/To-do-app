from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    #gives soem time of config setup for the application
    app=QApplication(sys.argv)
    #creatign window
    win=QMainWindow()
    #size of window
    win.setGeometry(200,200,300,300)
    win.setWindowTitle("My first GUI program!!")
    label = QtWidgets.QLabel(win)
    label.setText("My first label")
    label.move(50,50)

    #shows out window
    win.show()
    #this allows a clean exit
    sys.exit(app.exec_())

window()