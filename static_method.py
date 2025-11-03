#Static method
# a method that belnogs to a class rather than any object
# from that class(instance) usually used for general utility functions
# best for utility functions that do not need access to class data 
class car:
    no_wheel = 4
    def __init__(self,branch,price):
        self.brand = branch
        self.price = price
    def display(self):
        print(f"Car brand is {self.brand} and price is {self.price}")
    
    #static method
    @staticmethod
    def discount_display():
        print("Congrats you will be getting 10% discount")
    
    def number_type():
        print(car.no_wheel)


bmw = car("BMW","340298457982")
bmw.display()
car.number_type()
# discount_display() -> error
bmw.discount_display() # error (no error if we use keyword @staticmethod)
# car.discount_display()

class Employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position
    def get_info(self):
        return f"{self.name} = {self.position}"

    @staticmethod
    def is_valid_postion(postion):
        valid_postion=["Manager","Cashier","cook","janitor"]
        return postion in valid_postion
        
print(Employee.is_valid_postion("cook"))