class Parent:
    def show(self):
        print("Inside Parent")

class Child(Parent):
    def show(self):
        print("Inside Child")

obj1 = Parent()
obj2 = Child()

obj1.show()  # Output: Inside Parent
obj2.show()  # Output: Inside Child
