class A:
    def aws(self):
        print("aws")
class B(A):
    def aws(self):
        super(B, self).aws()
        print("I jeszcze to")
class C(A):
    def aws(self):
        super(C, self).aws()
        print("I to też")
# obiektB = B()
# obiektB.aws()
obiektC = C()
obiektC.aws()

