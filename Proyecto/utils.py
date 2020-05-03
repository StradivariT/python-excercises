def getSingleUserOption(msg: str, users: list) -> int:
    print(msg)

    for i in range(len(users)):
        print(f'{i + 1}. { users[i].name }')

    option = int(input()) - 1
    print("")

    return option

def getMultipleUsersOptions(msg: str, users: list) -> list:
    print(msg)

    for i in range(len(users)):
        print(f'{i + 1}. { users[i].name }')

    options = input()
    print("")

    return list(map(lambda x : int(x) - 1, options.split(",")))