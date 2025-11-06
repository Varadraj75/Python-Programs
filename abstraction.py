# Abstraction
# showing necessary details & hiding complex implementation.
#Rules:
# we have to implement parent abstract method in 

from abc import ABC,abstractmethod
class Car(ABC):
    @abstractmethod
    def Break():
        pass
    @abstractmethod
    def Ac():
        pass
    #concrete method
    def sunroof():
        pass

class worker1(Car):
    def Break():
        print("break implemented.")
    def Ac():
        print("Ac is working.")

worker1.Break()
worker1.Ac()


#Q4:- question in the class 
class shape(ABC):
    def __init__(self,c):
        self.color = c
    
    @abstractmethod
    def area(self):
        pass

    def display_color(self):
        pass

class Circle(shape):
    def __init__(self, r):
        self.radius = r
    
    def area(self):
        print(f"Area of circle is {3.14 * self.radius**2}")

class reactangle(shape):
    def __init__(self, l,b):
        self.length = l
        self.breadth =b 

    def area(self):
        print(f"Area of rectange is {self.length * self.breadth}")

co = Circle(20)
co.area()