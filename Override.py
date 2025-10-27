class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Woof, Woof")

class Cat(Animal):
    def speak(self):
        print("Meow, Meow")

def make_animal_speak(animal):
    animal.speak()

dog = Dog()
cat = Cat()

make_animal_speak(dog)
make_animal_speak(cat)
