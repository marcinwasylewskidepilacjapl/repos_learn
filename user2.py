class User:
    nextId = 1
    def __init__(self, name=""):
        self.name = name
        self.id = User.nextId
        User.nextId += 1

listOfUsers = [User() for i in range(8)]
for user in listOfUsers:
    print(user.id)

print("Następne id:", User.nextId)