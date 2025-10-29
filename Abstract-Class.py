from abc import ABC, abstractmethod

class RBI(ABC):

    @abstractmethod
    def roi(self,r):
        pass

class SBI(RBI):

    def show(self):
        print("Hello, I am SBI")
    def roi(self,r):
        print("The Rate Of Interest given by SBI is :",r)

class HDFC(RBI):

    def show(self):
        print("Hello, I am HDFC")
    def roi(self,r):
        print("The Rate Of Interest given by HDFC is :",r)

s=SBI()
s.show()
s.roi(6.5)

h=HDFC()
h.show()
h.roi(7.5)
