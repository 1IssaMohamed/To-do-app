from PyQt5.QtWidgets import * #importing all from widgets
from PyQt5.QtGui import QFont, QStandardItemModel, QStandardItem
from PyQt5 import uic
import pickle

#Qmain window from qt widget
class MyGUI(QMainWindow):

    def __init__(self):
        #sendign the class MyGUI into the super method of QMainWindow
        super(MyGUI,self).__init__()
        #loading the user index, form the todo thingy that we just created, then load it onto the self object
        uic.loadUi("todo.ui",self)
        #showing the self object, which not conatins the todo.ui
        self.show()

        self.setFixedSize(330,405)
        self.setWindowTitle("My todo applicaiton")

        #creating the item model so that we can actually see the list of tasks
        self.model=QStandardItemModel()
        #essentially this accessess the list view form the ui that we created in pyqt
        self.listView.setModel(self.model)

        #calls the diff functions on the diff calls
        self.plusButton.clicked.connect(self.add_todo)
        self.minusButton.clicked.connect(self.remove_todo)
        self.actionLoad.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)

    def add_todo(self):
        #creates an input dialoag that essentially takes the input of the text
        #QlineEdit creates the 1 line to do the writing, ig the last "" is for the stargin input
        todo,confirmed = QInputDialog.getText(self,"Add ToDo", "New Todo:", QLineEdit.Normal,"")
        #if we have confirmed a dialog adn the input isnt just all spaces we will make an item
        if confirmed and not todo.isspace():
            #create an item with the text that was just inputted
            item = QStandardItem(todo)
            self.model.appendRow(item)

    def remove_todo(self):
        #this is to avoid removing absolutely nothign 
        if len(self.listView.selectedIndexes())!=0:
            selected=self.listView.selectedIndexes()[0]

            dialog=QMessageBox()
            #this doubel checks if youw want to remove or nto
            dialog.setText(f"Are you sure you want to reomve '{selected.data()}'?")
            dialog.addButton(QPushButton("Yes"),QMessageBox.YesRole)
            dialog.addButton(QPushButton("No"), QMessageBox.NoRole)

            if dialog.exec_() ==0:
                self.model.removeRow(selected.row())

    def open_file(self):
        options=QFileDialog.Options()
        filename, _=QFileDialog.getOpenFileName(self,"Open File","","ToDo Files (*.todo)",options=options)
        if filename !="":
            #readign the bytes 
            with open(filename,"rb") as f:
                #loads everthign into a list
                item_list=pickle.load(f)
                self.model=QStandardItemModel()
                self.listView.setModel(self.model)
                for item in item_list:
                    self.model.appendRow(QStandardItem(item))

    def save_file(self):
        #need to create normal list to serialize then abck to gui lsit
        item_list=[]
        for x in range(self.model.rowCount()):
            item_list.append(self.model.item(x).text())
        options=QFileDialog.Options()
        #_= is a file filter or sum, this is just a normal diagol to get the file naem 
        filename, _=QFileDialog.getSaveFileName(self,"Save File","","ToDo Files (*.todo)",options=options)
        if filename !="":
            #writing the bytes of th elist now
            with open(filename,"wb") as f:
                #this leads to the item list being seriealized into the file name that we got from the dialog above
                pickle.dump(item_list,f)


#creating the applciation
app=QApplication([])
#showing the windwo
window=MyGUI()
#executign!
app.exec_()