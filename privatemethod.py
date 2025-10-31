class BankAccount:
    def __init__(self):
        __balance = 12000

    #public method (getter function)
    def manager(self):
        print(self.__balance)
    
    #public method (setter function)
    def scholorship(self,amt):
        self.__balance = amt

obj1=BankAccount()
obj1.scholorship(10024095235)
obj1.manager()
#class mangaling
print(obj1._BankAccount__balance)
# print(_BankAccount__balance)


# _BankAccount.__balance

