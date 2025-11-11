#prime number -> to check the prime number 

a = int(input("Enter a number to check wheather it is a prime number or not "))

flag = True
for i in range(2,a):
    if(a%i==0):
        flag = False
        break


if(flag):
    print("Prime number")
else:
    print("Not a prime ")


a = int(input("Enter the number "))

for i in range(2,a+1):
    flag = True
    for j in range(2,i):
        if(i%j==0):
            flag = False
            break
    if flag:
        print(i)


# another approach
import math
n=20
l=[True]*(n+1)
l[0]=l[1]=False

for i in range(2,int(math.sqrt(n))+1):
    for j in range(i*i,n+1,i):
        l[j]=False

for i in range(2,n+1):
    if(l[i]):
        print(i)