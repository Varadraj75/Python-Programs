#Abstract class

from abc import ABC, abstractmethod

class Vechile(ABC):
    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(Vechile):
     def go(self):
         print("you drive the car")
    
     def stop(self):
      print("You stop the car")

class motorcycle(Vechile):
    def go(self):
        print("You ride the motorcycle")
    def stop(self):
        print("You stop the motorcycle")

car = Car()
car.go()
car.stop()