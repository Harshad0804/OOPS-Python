class Tops:

    def admission(self,sname,snumber,course,fees):
        self.sname=sname
        self.snumber=snumber
        self.course=course
        self.fees=fees
        print ("Hello",sname)
        print("Your Mobile Number",snumber)
        print("Your Course Is",course)
        print("Fees Of Your Course is",fees)

    def finstallment(self,amount):
        self.fees=self.fees-amount
        print("Your pending fees",self.fees)

    def sinstallment(self,amount):
        self.fees=self.fees-amount

    def tinstallment(self,amount):
        self.fees=self.fees-amount

    def remainingfees(self,amount):
        self.fees=self.fees-amount
        print("your Remaining Fees",self.fees)
        

t1=Tops()

#t1.admission("Karguwal Harshad",9601119229,"Python-Developer",100000)

while True:
    print("*"*50)
    print("1. Check Student Details")
    print("2. Pay Fees")
    print("3. Remaining Fees")
    print("4. Exit")

    choice=int(input("Enter Your Choice : "))
    print("*"*50)

    if choice==1:
        t1.admission("Karguwal Harshad",9601119229,"Python-Developer",60000)
    elif choice==2:
        amount=int(input("Enter Your Fees Amount : "))
        t1.finstallment(amount)
    elif choice==3:
        t1.remainingfees(amount)
    elif choice==4:
        print("Thank You...!   SEE YOU SOON   ")
    else:
        print("Invalid Choice! Please Try Again")
        
        
        
        
        
