# Scope of the variable 


# A is the global variable
i = 1 
factorial = int(input("Enter the value "))

def factoria(factorial):
    if(factorial == 0):
        print("1")
    else:
        factorial =1
        for i in range(1,factorial):
            # factorial is the local variable here , we can't access outside the function
            factorial = factorial*i
        return factorial

print(factoria(factorial))

#global variables cannot be modified in local scope. 

a=10 
a = a+10 
print(a)
def sqrt(n):
    global a
    a=a+4
    print(a)
    b=50
    print(b)

sqrt(20)
print(a)
#b is present in the local scope
# print(b)

# Arguments:- 
# 1. Positional arguments:
def sub(a,b):
    print(a-b)

a=2
b=3
sub(a,b)
sub(b,a)
