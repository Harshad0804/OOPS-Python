class MyNumber:
    def __init__(self, value):
        self.value = value  

    def __add__(self, other):
        if isinstance(other, MyNumber):
            return MyNumber(self.value + other.value)
        return MyNumber(self.value + other)

    def __str__(self):
        return f"MyNumber({self.value})"

    def double(self):
        return self.value * 2

num1 = MyNumber(10)
num2 = MyNumber(5)
num3 = num1 + num2   
print(num3)         
print(num1.double())
