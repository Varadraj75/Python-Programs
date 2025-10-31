#protected 
# it is not accessable for outside of theclass but we access inside the subclass
class hari:
    def __init__(self):
        self._balance=15000
    
    def display(self):
        print(f"Balance of hari is{self.balance}")


class Krishna(hari):
    def display_info(self):
        print(f"Balance of father is {self._balance}")

obj1 = Krishna()
obj1.display_info()
print(obj1._balance)

