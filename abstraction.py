# Abstraction
# showing necessary details & hiding complex implementation.
#Rules:
# we have to implement parent abstract method in 

from abc import ABC
class Car(ABC):
    def Break():
        pass
    def Ac():
        pass
    def sunroof():
        pass

class worker1(Car):
    def Break():
        print("break implemented.")
    def Ac():
        print("Ac is working.")