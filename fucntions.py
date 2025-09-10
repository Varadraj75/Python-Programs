#Function 
# Code blocks which are created to increase resuabilty , understandable , modularity and cleanliness 
# Dry :- Don't repeat yourself

# import random , in these random is the module 

# Syntax: 
# def name_of_function(args/perameters):
#   pass

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