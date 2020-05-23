from PyQt5.QtWidgets import QApplication
import json
import sys

from user import User
from ui import UI
from crud import CRUD

def loadLocalDatabase() -> list:
    usersFile = open("./Proyecto/database/db.json", "r")
    usersDict = json.loads(usersFile.read())
    usersFile.close()

    return list(map(lambda x: User.fromDict(x), usersDict))

def main():
    app = QApplication(sys.argv)
    
    users = loadLocalDatabase()

    crud = CRUD(users)
    ui = UI(crud, users)

    ui.show()

    sys.exit(app.exec_())

main()