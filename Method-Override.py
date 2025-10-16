class A:
    def show(self):
        print("Show From A")
class B(A):
    def show(self):
        print("Show From B")
class C(B):
    def show(self):
        print("Show From C")

c1=C()
c1.show()


class X:
    def show(self):
        print("Show From X")
class Y(X):
    def show(self):
        super().show()
        print("Show From Y")
class Z(Y):
    def show(self):
        super().show()
        print("Show From Z")

z1=Z()
z1.show()
