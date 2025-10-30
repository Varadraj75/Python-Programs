class BankAccount:
    accountNumber =0
    balance=0.0

    def __init__(self,a,b):
        self.accountNumber = a
        self.balance=b
    def withdraw(self,amt):
        if(amt>self.balance):
            raise RuntimeError("Insufficent Balance")
        if(amt<0):
            raise ValueError("invalid input")
        
        self.balance -= amt
        print(self.balance)




p1 = BankAccount(1234,900000)
try:
 try:
     try:
        p1.withdraw(1500)
     except RuntimeError as msg:
        print(msg)
 except ValueError as msg:
    print(msg)
except Exception:
   print("Unknown error")
