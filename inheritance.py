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
    def __init__(self, b, c,d):
        super().__init__(b,c,)
        self.typres = d
    
    def no_wheels(self):
        print(f"Number of wheels {self.typres}")

obj = car(10,20,4)
obj.no_wheels()
obj.key()
obj.Break()

#types of inheritance 
# 1) Single inheritance -> parent and child
# 2) Multiple inheritance -> 2 parent and one child
# 3) Multi Level inheritance -> grandparent - parent - child
# 4) Hierarchical Inheritance -> 1 parent 2 child
# 5) Hybrid Inheritance -> parent - child 1 child 2 - parent (diamond style)