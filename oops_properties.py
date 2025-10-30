#OOPS -> object oriented programming
#Encapsulation-> hides the some or required details and won't be accessed outside of the class 
#wrapping data and methods together into a single unit (class)
# and restricting direct access to some parts of an object.
# used by __ as prefix for private in encapsulation

class person:
    def __init__(self):
        #public attribute
        self.name="hari"
        #private attribute
        self.__atmpin = "4321"
    #public method
    def print_info(self):
        print("Information about the person")
    #private method
    def __display(self):
        print("Display info about person")
    
    #getter function
    def ge_atmpin(self):
        print(self.__atmpin)

    #setter function
    def se_atmpin(self , new_pin):
        self.__atmpin = new_pin


p1= person()
# print(p1.name)
# print(p1.atmpin)
p1.se_atmpin(2358) #updated the private attribute
p1.ge_atmpin() # accessed the private attribute