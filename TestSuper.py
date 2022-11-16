# Metoda super odwoluje sie do kolejnej klasy niżej w dziedziczeniu
# Np mamy C-B-A-Ap
# Jesli stworze obiekt w C i tam uzyje super() to == super(C,self) odwola sie do klady nizej
# super(B, self) odwola sie do A
# super(A, self) odwola sie do Ap


class Ap:
    def printing(self):
        print("Podklasa")

class A(Ap):
    def printing(self):
        super().printing()
        print("A")
class B(A):
    def printing(self):
        print("Zaczynam B")
        super().printing()
        print("Dziedzicze jak widac po A")
class C(B):
    def printing(self):
        super(A, self).printing()
        print("A ciekawe co teraz")

obj = C()
obj.printing()
"""Wynik bedzie: Podklasa, A ciekawe co teraz"""


# class A:
#     def printing(self):
#         print("A")
# class B(A):
#     def printing(self):
#         print("Zaczynam B")
#         super().printing()
#         print("Dziedzicze jak widac po A")
# class C(B):
#     def printing(self):
#         super(C, self).printing()
#         print("A ciekawe co teraz")
# obj = C()
# obj.printing()
# """Wynik będzie taki sam jakbym nie wpisal w super nic czyli Zaczynam B, A, Dziedzicze jak widac po A, A ciekawe co teraz"""

# class A:
#     def printing(self):
#         print("A")
# class B(A):
#     def printing(self):
#         print("Zaczynam B")
#         super().printing()
#         print("Dziedzicze jak widac po A")
# class C(B):
#     def printing(self):
#         super(B, self).printing()
#         print("A ciekawe co teraz")
# obj = C()
# obj.printing()
# """Wynik będzie: A, A ciekawe co teraz"""