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

a=4
b=3
sub(a,b) #correct
sub(b,a) #incorred

#2. Keyword arguments: order/position does not matter 

def subtract(a,b):
    print(a-b)

# Substract b from a 
# in these both the statements are correct 
subtract(a=2,b=3)  #correct
subtract(b=3 , a=2) #correct 


#3. Default arguments
def subt(a=2,b=3):
    print(a-b)

subtract(5,5) 
# the passed values are overriding the default values
# 0 is the answer 


#Q1:- Write a funtion that takes marks of 5 subjects and returns total and average.
a = int(input("Enter the subject 1"))
b = int(input("Enter the subject 2"))
c = int(input("Enter the subject 3"))
d = int(input("Enter the subject 4"))
e = int(input("Enter the subject 5"))

def subject(a,b,c,d,e):
    avg = a+b+c+d+e / 5
    total = a+b+c+d+e
    # print(f"The avg of 5 subjects are {avg}")
    # print(f"The total of 5 subject are {total}")
    return avg,total

average,total = subject(a,b,c,d,e)

# Q2:- Write a function that takes an integer and returns true if it's a palindrome 
# (reads the same forwards and backwards), otherwise False. 
# use only loops and conditionals.
 

# n = 42 
# rev_n = 0 

# rev_n = rev_n*10 + n%10 
# n //= 10 
# # rev_n contains 2 
# # n contains 4 

# rev_n = rev_n*10 + n%10 
# n //= 10 
def reverse_int(n):
    rev_n=0
    while n!=0:
        rev_n = rev_n*10 + n%10
        n //=10 
    print(rev_n)

n= int(input("Enter an integer: "))
reverse_int(n)
# palindrome number : 121 -> 121

def is_palindrome(n):
    rev_n = reverse_int(n)
    # palindrome number : 121 -> 121
    if n == rev_n:
        print("Yes it is palindrome")
    else:
        print("No")
