#Question for class
#Q1:
class Laptop:
    def __init__(self,brand,price):
        print(f"{brand} is the laptop brand and the price is {price}")
        print(f"{brand} Laptop is now ON!")
        

Laptop("apple",10000)
Laptop("hp",100)

#Q2:-
class Employee:
    def __init__(self,n,s,d):
        self.name = n 
        self.salary=s
        self.department=d

    def bonus(self):
        if(self.department=="sales"):
            self.salary += self.salary*0.1
        else:
            self.salary += self.salary*0.05
    
    def display(self):
        print(self.name)
        print(self.salary)
        print(self.department)



l1 = Employee("Varad",10000,"sales")
l1.bonus()
l1.display()
l2= Employee("Varad",10000,"management")
l2.bonus()
l2.display()

#Q3:- calculator
class calculator:

    def addition(self,a,b):
        print(a+b)
    def subtraction(self,a,b):
        print(b-a)
    def multiplication(self,a,b):
        print(a*b)
    def division(self,a,b):
        print(a/b)

c1 = calculator()
c1.addition(10,20)
c1.subtraction(10,20)
c1.multiplication(10,20)
c1.division(20,10)

#Q4:- BankAccount
class InsucificentFunds(Exception):
         pass
class BankAccount:
    def __init__(self):
        self.AccountNumber=int(input("Enter the number"))
        self.Account_holder_name=input("Enter the name")
        self.balance=float(input("Enter the balance"))
    def withdraw(self):
        self.withdra = float(input("Enter the withdraw amount"))
        try:
            if(self.withdra > self.balance):
                raise InsucificentFunds("It has insucificent funds")
        except InsucificentFunds as msg:
            print(msg)
        else:
            print("fund is withdraw")
        
b1 = BankAccount()
b1.withdraw()
