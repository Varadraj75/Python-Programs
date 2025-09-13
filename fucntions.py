#Function 
# Code blocks which are created to increase resuabilty , understandable , modularity and cleanliness 
# Dry :- Don't repeat yourself

# Q:- what are the types of function?
# Answer:- perameter or function
# Defination:- 1) Built in 
# 




# import random , in these random is the module 

# Syntax: 
# def name_of_function(args/perameters):
#   pass

#print("varad" , "ravi" , "nathan" , sep="@" , end="/" , flush =True)

#print(obj,sep,end,flush)
#flush by default value is true
#

import random

#Q1:- Write a function to perform addition of two intergers a and b 

a = int(input("Enter the value of a "))
b = int(input("Enter the value of b 1"))

def add(a,b):
    return (a+b)


print(add(a,b))



#Q2:- write a fucntion greet(name) that prints a personalized greeting message. 
name = input("Enter the name")

def greet(name):
    print(f"{name} Hey welcome to PST")
    return (f"{name} Hey welcome to PST")

print(greet(name))

#Q3:- Write a function square (num) that returns the square of a number. 

num = int(input("Enter a num "))

def square(num):
    return(num*num)

print(square(num))


#Q4:- WAF that returns both the area and perimeter of a rectangle 

len = int(input("Enter the length of the rectangle"))
wid = int(input("Enter the width of the rectangle"))

def tra(len,wid):
    area = len*wid
    peri = 2*(len+wid)
    return area,peri
    
# positional arrguments 
print(tra(len,wid))

#Q5:- WAF factorial(n) that returns the factorial of a number. 

fact = int(input("Enter the factorial"))

def factorial(fact):
    i = 1 
    faci = 1 
    for i in range(1,fact+1):
        fact *= i
    return faci

print(fact)