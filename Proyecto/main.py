import json

from user import User
import local_crud as c
import file_generation as f

def getMainMenuOption() -> int:
    print("""Hi, please select one of the following:
    1. Add a new user
    2. Display a single user
    3. Display all users
    4. Display some users
    5. Modify a user
    6. Delete a user
    7. Generate file for single user
    8. Generate files for all users
    9. Generate files for some users
    10. Exit""")

    return int(input())

def loadLocalDatabase() -> list:
    usersFile = open("./Proyecto/database/db.json", "r")
    usersDict = json.loads(usersFile.read())
    usersFile.close()

    return list(map(lambda x: User.fromDict(x), usersDict))

def main():
    users = loadLocalDatabase()

    while (True):
        option = getMainMenuOption()
        print("")
        
        {
            1: lambda: c.addNewUser(users),
            2: lambda: print(c.getSingleUser(users)),
            3: lambda: print(c.getAllUsers(users)),
            4: lambda: print(c.getSomeUsers(users)),
            5: lambda: c.modifyUser(users),
            6: lambda: c.deleteUser(users),
            7: lambda: f.generateFileForSingleUser(users),
            8: lambda: f.generateFileForAllUsers(users),
            9: lambda: f.generateFileForSomeUsers(users),
            10: exit,
        } [option]()
        print("")

main()