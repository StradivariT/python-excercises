from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QListWidget, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox

from crud import CRUD

class UI(QMainWindow):
    def __init__(self, crud: CRUD, users: list):
        super(UI, self).__init__()

        self.crud = crud
        self.users = users

        self.setupUI()

    def setupUI(self):
        self.setGeometry(400, 200, 800, 550)
        self.setWindowTitle("Register users app")

        self.popUp = QMessageBox()

        # Users List
        usersLabel = QLabel("Users registered", self)
        usersLabel.resize(120, 30)
        usersLabel.move(50, 30)

        self.usersList = QListWidget(self)
        self.usersList.setFixedSize(300, 300)
        self.usersList.move(50, 60)
        self.updateUsersList()

        # New User Form
        newUserLabel = QLabel("Register new user", self)
        newUserLabel.resize(200, 30)
        newUserLabel.move(400, 30)

        newNameLabel = QLabel("Name", self)
        newNameLabel.resize(80, 30)
        newNameLabel.move(400, 60)

        self.newNameBox = QLineEdit(self)
        self.newNameBox.resize(100, 20)
        self.newNameBox.move(445, 65)

        newEmailLabel = QLabel("Email", self)
        newEmailLabel.resize(50, 30)
        newEmailLabel.move(580, 60)

        self.newEmailBox = QLineEdit(self)
        self.newEmailBox.resize(150, 20)
        self.newEmailBox.move(625, 65)

        newPhoneLabel = QLabel("Phone", self)
        newPhoneLabel.resize(50, 30)
        newPhoneLabel.move(400, 100)

        self.newPhoneBox = QLineEdit(self)
        self.newPhoneBox.resize(100, 20)
        self.newPhoneBox.move(445, 105)

        newAddressLabel = QLabel("Address", self)
        newAddressLabel.resize(80, 30)
        newAddressLabel.move(580, 100)

        self.newAddressBox = QLineEdit(self)
        self.newAddressBox.resize(140, 20)
        self.newAddressBox.move(635, 105)

        self.newUserButton = QPushButton("Register", self)
        self.newUserButton.resize(80, 25)
        self.newUserButton.move(390, 140)
        self.newUserButton.clicked.connect(self.addNewUser)

        # Modify User Form
        modifyUserLabel = QLabel("Modify user with index", self)
        modifyUserLabel.resize(160, 30)
        modifyUserLabel.move(400, 190)

        self.modifyIndexBox = QLineEdit(self)
        self.modifyIndexBox.resize(100, 20)
        self.modifyIndexBox.move(550, 195)

        modifyNameLabel = QLabel("Name", self)
        modifyNameLabel.resize(50, 30)
        modifyNameLabel.move(400, 220)

        self.modifyNameBox = QLineEdit(self)
        self.modifyNameBox.resize(100, 20)
        self.modifyNameBox.move(445, 225)

        modifyEmailLabel = QLabel("Email", self)
        modifyEmailLabel.resize(50, 30)
        modifyEmailLabel.move(580, 220)

        self.modifyEmailBox = QLineEdit(self)
        self.modifyEmailBox.resize(150, 20)
        self.modifyEmailBox.move(625, 225)

        modifyPhoneLabel = QLabel("Phone", self)
        modifyPhoneLabel.resize(50, 30)
        modifyPhoneLabel.move(400, 260)

        self.modifyPhoneBox = QLineEdit(self)
        self.modifyPhoneBox.resize(100, 20)
        self.modifyPhoneBox.move(445, 265)

        modifyAddressLabel = QLabel("Address", self)
        modifyAddressLabel.resize(80, 30)
        modifyAddressLabel.move(580, 260)

        self.modifyAddressBox = QLineEdit(self)
        self.modifyAddressBox.resize(140, 20)
        self.modifyAddressBox.move(635, 265)

        self.modifyUserButton = QPushButton("Modify", self)
        self.modifyUserButton.resize(80, 25)
        self.modifyUserButton.move(395, 300)
        self.modifyUserButton.clicked.connect(self.modifyUser)

        # Delete User Form
        deleteUserLabel = QLabel("Delete user with index", self)
        deleteUserLabel.resize(150, 30)
        deleteUserLabel.move(400, 340)

        self.deleteIndexBox = QLineEdit(self)
        self.deleteIndexBox.resize(100, 20)
        self.deleteIndexBox.move(550, 345)

        self.deleteUserButton = QPushButton("Delete", self)
        self.deleteUserButton.resize(80, 25)
        self.deleteUserButton.move(660, 340)
        self.deleteUserButton.clicked.connect(self.deleteUser)

        # File Generation stuff
        fileLabel = QLabel("Generate file/s as", self)
        fileLabel.resize(200, 30)
        fileLabel.move(50, 390)

        self.plainCheck = QCheckBox("Plain text", self)
        self.plainCheck.resize(100, 30)
        self.plainCheck.move(50, 420)

        self.pdfCheck = QCheckBox("PDF", self)
        self.pdfCheck.resize(100, 30)
        self.pdfCheck.move(50, 450)

        self.wordCheck = QCheckBox("Word", self)
        self.wordCheck.resize(100, 30)
        self.wordCheck.move(50, 480)

        userSelectLabel = QLabel("For users with indexes separated by comma, or all users", self)
        userSelectLabel.resize(380, 30)
        userSelectLabel.move(220, 390)

        fileIndexesLabel = QLabel("Indexes", self)
        fileIndexesLabel.resize(60, 30)
        fileIndexesLabel.move(220, 420)

        self.fileIndexesBox = QLineEdit(self)
        self.fileIndexesBox.resize(100, 20)
        self.fileIndexesBox.move(280, 425)

        self.allUsersCheck = QCheckBox("All users(this overwrites indexes above if any was provided)", self)
        self.allUsersCheck.resize(400, 30)
        self.allUsersCheck.move(220, 450)

        self.fileButton = QPushButton("Generate", self)
        self.fileButton.resize(80, 25)
        self.fileButton.move(215, 490)
        self.fileButton.clicked.connect(self.generateFiles)

    def updateUsersList(self):
        self.usersList.clear()
        list(map(lambda x: self.usersList.addItem(f'''{ x[0] }: { x[1] }'''), enumerate(self.users)))

    def displayPopUp(self, msg: str):
        self.popUp.setText(msg)
        self.popUp.exec_()

    def addNewUser(self):
        if (self.newNameBox.text() == "" or self.newEmailBox.text() == "" or self.newPhoneBox.text() == "" or self.newAddressBox.text() == ""):
            self.displayPopUp("Please, fill all the fields on the form")
            return

        self.crud.addNewUser(self.newNameBox.text(), self.newEmailBox.text(), self.newPhoneBox.text(), self.newAddressBox.text())
        self.updateUsersList()

        self.newNameBox.clear()
        self.newEmailBox.clear()
        self.newPhoneBox.clear()
        self.newAddressBox.clear()

        self.displayPopUp("User registered successfully!")
    
    def modifyUser(self):
        if (self.modifyIndexBox == "" or self.modifyNameBox.text() == "" or self.modifyEmailBox.text() == "" or self.modifyPhoneBox.text() == "" or self.modifyAddressBox.text() == ""):
            self.displayPopUp("Please, fill all the fields on the form")
            return
        
        err = self.crud.modifyUser(int(self.modifyIndexBox.text()), self.modifyNameBox.text(), self.modifyEmailBox.text(), self.modifyPhoneBox.text(), self.modifyAddressBox.text())
        if (err != ""):
            self.displayPopUp(err)
            return

        self.updateUsersList()

        self.modifyIndexBox.clear()
        self.modifyNameBox.clear()
        self.modifyEmailBox.clear()
        self.modifyPhoneBox.clear()
        self.modifyAddressBox.clear()

        self.displayPopUp("User modified successfully!")

    def deleteUser(self):
        if (self.deleteIndexBox.text() == ""):
            self.displayPopUp("Please, fill all the fields on the form")
            return

        err = self.crud.deleteUser(int(self.deleteIndexBox.text()))
        if (err != ""):
            self.displayPopUp(err)
            return

        self.updateUsersList()
        self.deleteIndexBox.clear()
        self.displayPopUp("User deleted successfully!")

    def generateFiles(self):
        if (not self.plainCheck.isChecked() and not self.pdfCheck.isChecked() and not self.wordCheck.isChecked()):
            self.displayPopUp("Please, select at least one file format")
            return

        if (self.fileIndexesBox.text() == "" and not self.allUsersCheck.isChecked()):
            self.displayPopUp("Please, provide at least one user index or select all users")
            return

        err = self.crud.generateFiles(self.fileIndexesBox.text(), self.allUsersCheck.isChecked(), self.plainCheck.isChecked(), self.pdfCheck.isChecked(), self.wordCheck.isChecked())
        if (err != ""):
            self.displayPopUp(err)
            return

        self.fileIndexesBox.clear()
        self.plainCheck.setChecked(False)
        self.pdfCheck.setChecked(False)
        self.wordCheck.setChecked(False)
        self.allUsersCheck.setChecked(False)

        self.displayPopUp("File/s generated successfully!")