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

obj1=worker1()
worker1.Break()
worker1.Ac()