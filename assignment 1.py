# Hierarchical Inheritance -> 1 parent 2 child 

class parent():
    def __init__(self):
        self.name = input("Enter your name")
        self.age = input("Enter your age")
        self.clas  = input("Enter your class")
        print(self.name)
        print(self.age)
        print(self.clas)

class child1(parent):
    def __init__(self):
        super().__init__()

class child2(parent):
    def __init__(self):
        super().__init__()


obj1 = child1()
obj2 = child2()


# Hybrid Inheritance ->  parent - child 1 child 2 - parent (diamond style)

class parent():
    def __init__(self):
        self.name = input("Enter your name")
        self.age = input("Enter your age")
        self.clas  = input("Enter your class")
        print(self.name)
        print(self.age)
        print(self.clas)

class child1(parent):
    def __init__(self):
        print("Child1 Constructor")
        super().__init__()

class child2(parent):
    def __init__(self):
        print("Child2 Constructor")
        super().__init__()

class parent2(child1,child2):
    def __init__(self):
        print("Parent2 Constructor")
        super().__init__()

obj3 = parent()
obj4 = child1()
obj5 = child2()
obj6 = parent2() 