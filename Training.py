class UserType1:
    age = 0
    name = "None"
    surname = "None"
    def set_name(self):
        self.name = input()
        self.name = str.capitalize(self.name)
    def set_surname(self):
        self.surname = input()
        self.surname = str.capitalize(self.surname)
    def set_age(self):
        self.age = int(input())
    def print_data(self):
        print(self.name, self.surname, self.age, "lat")
class UserType2:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
    def print_data(self):
        print(self.name, self.surname, self.age, "lat")
    def __str__(self):
        return self.name + " " + self.surname
if __name__ == '__main__':

    #sposob1
    person1 = UserType1()
    person2 = UserType1()

    person1.set_name()
    person1.set_surname()
    person1.set_age()
    person1.print_data()

    person2.print_data()

    #sposob2

    a = "Robert"
    b = "Lewandowski"
    c = 27

    person_1 = UserType2(a,b,c)
    person_1.print_data()
    print(f"{len(b)}; {b.__len__()}")
    print(person_1)