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