import json

import utils as u
from user import User

def addNewUser(users: list):
    users.append(User.fromInput())
    saveUsers(users)

def getSingleUser(users: list) -> str:
    if User.isEmpty():
        return "There are no users registered"

    return users[u.getSingleUserOption("Pick which user you want to get more info:", users)]

def getAllUsers(users: list) -> str:
    if User.isEmpty():
        return "There are no users registered"

    result = ""
    for user in users:
        result += str(user) + "\n"

    return result.strip()

def getSomeUsers(users: list) -> str:
    if User.isEmpty():
        return "There are no users registered"

    options = u.getMultipleUsersOptions("Pick which users you want to get more info separated by commas, ex. 1,2,...:", users)

    result = ""
    for option in options:
        result += str(users[option]) + "\n"

    return result.strip()

def saveUsers(users: list):
    jsonStr = json.dumps([user.__dict__ for user in users])
    
    db = open("./Proyecto/database/db.json", "w")
    db.write(jsonStr)
    db.close()

def modifyUser(users: list):
    if User.isEmpty():
        print("There are no users registered")
        return 

    option = u.getSingleUserOption("Pick which user you want to modify:", users)

    users[option].modify()
    saveUsers(users)

    print("User modified")

def deleteUser(users: list):
    if User.isEmpty():
        print("There are no users registered")
        return 

    option = u.getSingleUserOption("Pick which user you want to delete:", users)

    del users[option]
    saveUsers(users)

    print("User deleted")