# Iterative Statements:
# We have curtain set of instruction and we want to iterated over certain set of instructions , then we use 
# iteration statements 

# For loop , while loop , do while loop.

# 1. For loop:
# print("Varad")

# Q1:- Print your names 10 times.
#Syntax: for iterator in range(start,end): this loop starts from start and ends at end-1 ,
#  Where iterator is a integer value

for i in range(0,10):
    print(i+1,"Varad")
print("")
# in these if we don't give the start point also the code starts from 0 as we don't have initialize anything
for i in range(10):
    print("Varad -",i+1)
print('')

#Q2:- print only even number from 1 to 10 

for i in range(2,11):
    if(i%2==0):
        print(f"{i} is a even number")
#Syntax: for iterator in range(start,end,step) , by default step is 1
print("")
for i in range(2,11,1):
    if(i%2==0):
        print(f"{i} is a even number")


#Q3:- Find the sum of first n natural numbers and print the sum 
n = int(input("Enter the n numbers "))
sum=0
for i in range (0,n+1):
    sum +=i

print(sum)

# 2.While-loop: 
# while condition:
# Statements 
# print name using while loop 

i=0
while i<10:
    print("varad")
    i +=1


j=0
while j<11:
    if(j%2==0):
        print(f"{j} is the even number")  
    j += 1


k= int(input("Please enter the number"))
sum=0
i=0
while i<=k:
    sum = sum+i
    i += 1

print(sum)

#Q6:- factorial of a number 
      #using for loop 
fac = int(input("Input the number"))
i=1
faci =1
for i in range(1,fac+1):
    faci *= i

print(faci)

     #using while loop 
fac = int(input("Enter the number"))
i , faci = 1,1 
while i<=fac:
    faci *=i
    i = i+1
print(faci)

#Q7:- Fibonacci Series 
nth = int(input("Find nth term of fibonacci series"))
n1 , n2 = 0,1
print(n1)
print(n2)
for i in range(2,nth):
    c=n1+n2
    print(c)
    n1=n2
    n2=c 
    
    