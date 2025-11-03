#Inheritance  -> taking the property of the parents
# child class has access of parent class asttributes & methods

class vehicle:
    def __init__(self,b,c):
        self.brand = b
        self.color = c
    
    def key(self):
        print("Vechicle is started")
    
    def Break(self):
        print("Vechile is stopped")

class car(vehicle):
    pass

obj = car(10,20)
obj.key()
obj.Break()

#types of inheritance 
# 1) Single inheritance
# 2) Multiple inheritance
# 3) Multi Level inheritance
# 4) Hierarchical Inheritance
# 5) Hybrid Inheritance