# Polymorphism 
# -> Concept under oops, where function(method) , attribute will behave differently based on the situation 
# compile time polymorphism (method overloading)
# Run time polymorephism (method overriding)
# 1) Compile Time

class parent:
    def display(self):
        print("Parent class")
    
class child:
    def display(self):
        print("child class")

obj_child = child()
child().display()

obj_parent = parent()
obj_parent.display()

# 2) Run-time 