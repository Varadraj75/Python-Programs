# Given three integers a,b,c find maximum of three and print it 

a = int(input("Enter the value")) 
b = int(input("Enter the value"))
c = int(input("Enter the value"))

# if(a>b):
#     if(a>c):
#         print(f"{a} is the max")
# elif(b>a):
#     if(b>c):
#         print(f"{b} is the max value")
# elif(c>a):
#     if(c>b):
#         print(f"{c} is the max value")
# elif(a==b==c):
#     print(f"{a} is the max value")


if(a>=b and a>=c):
    print(f"{a} is the max")
elif(b>=a and b>=c):
    print(f"{b} is the max")
else:
    print(f"{c} is the max ")


print(max(a,b,c))


#Given 4 integers a,b,c,d find max of these 4.
a = int(input("Enter the value ")) 
b = int(input("Enter the value "))
c = int(input("Enter the value "))
d = int(input("Enter the value "))

if(a>=b and a>=c and a>=d):
    print(f"{a} is the max ")
elif(b>=a and b>=c and b>=d):
    print(f"{b} is the max ")
elif(c>=a and c>=b and c>=d):
    print(f"{c} is the max ")
else:
    print(f"{d} is the max ")


# Leap year or not 

leap = int(input("Enter the year"))

if(leap%400==0 or (leap%4==0 and leap%100 != 0)):
        print("Leap year")
else:
    print("Not leap year")