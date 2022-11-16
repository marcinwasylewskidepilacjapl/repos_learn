class User:
    Last_id = 0 #zmienna statyczna/klasowa
    def __init__(self, name):
        self.name = name
        User.Last_id += 1
        self.id = User.Last_id
a = User("Arkadiusz")
b = User("Wiola")
c = User("Marcin")


lista = [a,b,c]
for name in lista:
    print(name.id)

print(User.Last_id)
