import math #importing math library 
#lib_name.function_name(arguments)

#Operators: used to perform operations over the data / manipulate the data 
#Operands: Values/Variables on which operators performs manipulations


a=5
b=6
sum =  a+b*3/3


#Type of operators:
# 1. Arithematic Operators: + , - , * , / , % , //
div = a/b
#// = floor value
divv = a//b 
print(div)
# if we have interger value than the floor and ceil value will be the same 
# math.floor(a/b) = round to the down value
# math.ceil(a/b) = round to the up value


#modulus 
mod=a%b
print(mod)

# Exponentiation:
# a^b => a**b 
# a is the base and b is the exponent/power
exp = a**b
print(exp)


#Example: a=10 , b =10
exp = 10**10
print(exp)

# given a and b , find a^b such that the answer should not exceed 100007. 

#in one second the complier performs 10^8 operation 
aa= 10
bb = 57575
ans = (aa**bb)%10007
print("hey",ans)


"""
2. Assignment Operators 

"""

#Q2:-  take two int and swap them without using and extra variable
a=3
b=4
temp = a
a=b
b=temp


print(a,b)
a,b = b,a
print(a,b)


#given a,b,c print true if a>b and b>c otherwise print false 
# using and operators , so true and true gives true , False and false gives false , true and false gives false
a=10
b=5
c=3
print((a>b) and (b>c) and (a>c))

#using or operators , so if the expression is true and true gives true , true and false is true , false and falase is flase 
# OR operators 
# exp 1 or exp 2
# T or T = T 
# T or F = T
# F or T = T 
# F or F = F 

print((a<b or (a>c)))

# Not operators , it just reverse the result , if true than false , if false than true 
print(not(a<b or (a>c)))







#Q3:- Take Principal amount , rate of interest , and time (in years ) as integers inputs and calculate simple interest

Principal = int(input("Enter the principal amount"))
rateOfInterest = int(input("Enter the ROI"))
time = int(input("Enter the years"))

simpleInterest = Principal*rateOfInterest*time / 100
print("The Simple Interest is " , simpleInterest)


# Q4:- wap to take the basic salary as int input and calculate the total salary ,
#  assuming house rent allowance (HRA) is 20% of basic and travel allownce (TA) is 10% of basic 
basic_salary = float(input("Enter your base salary"))
HRA = float(input("Enter the house rent allowance "))
Ta = float(input("Enter the travel allownce "))

HRA = basic_salary/100 * 20
Ta = basic_salary/100 * 10

total_salary = basic_salary+HRA+Ta
print(total_salary)


#Q5:- wap to take coordinates of two points (x1,y1) and (x2 , y2) . calculate the distance between them using the distance formula.

x1 = float(input("Enter the x1 value"))
x2 = float(input("Enter the x2 value"))
y1 = float(input("Enter the y1 value"))
y2 = float(input("Enter the y2 value"))

distance = math.sqrt(math.pow(x2-x1,2)+math.pow(y2-y1,2))

print(distance)



#Q6:- A student enteres marks for 3 subjects as strings. convert them to int and calculate the avg 

sub_1= str(input("Enter the marks in maths "))
sub_2 = str(input("Enter the marks in physics"))
sub_3 = str(input("Enter the marks in chemistry"))

sub_1 = int(sub_1)
sub_2 = int(sub_2)
sub_3 = int(sub_3)

print(f"Score in maths {sub_1}")
print(f"Score in physics {sub_2}")
print(f"Score in chemistry {sub_3}")

avg= sub_1+sub_2+sub_3 / 3
print(f"The average score is {avg}")

#Q7:- Take a number age = 25. convert it into a string and print "My age is 25". 

age = 25 
age = str(age)
print(f"My age is {age}")
# we can concinate because it is string
print("My age is " + age)

#Q8:- A shopping site shows price as string "499.99". Add delivery charge (50 as int) and print the final bill 

price = "499.99"
price= int(499.99) + 50
print(price)

#Q9:- take a complex number z=5+2j . convert it into string . extract real and imaginary parts as integers print their sum 

z= str(5+2j)
z_real = z.split('+')[0].strip()
z_imaginary= z.split('+')[1]
sum_complex = ( z_real + z_imaginary)
print(sum_complex)



# Bitwise Operators:
# 4: 0100
# 2: 0010
# note in ipad 

#Q10:- A pen costs 12 , a notebook costs 45. if u buy 3 pens and 4notebooks , find the total cost 
pen=12
notebook = 45

pen = 3*pen
notebook = 4*notebook
totalcost = pen + notebook
print(totalcost)


#Q11:- A sudent scored 78 marks in maths . the passing mark is 40 . check and print whether the student passed. Print true or false accordingly

score = 78 
passing_mark = 40 
check = (score>=passing_mark)
print(f"The result is {check}")


# Q12:- An exam allows a candidate to pass if: marks in theory >= 40 AND marks in practical >=20 , 
# check if a student with theory = 55 , practical = 15 , passed or failed 
theory = 55
practical = 155
theory = (theory>=40)
practical = (practical >=20)
print("the result is" ,theory and practical)



#Q13:- Check if a letter exicts in a given word.  word="PYTHON"
a = "a"
word = "Python"
print(a is word)


#Identity operators -> to check the identity of the two variables 
a=2
b=2
print(a is b)
print(a is not b)


#Membership Operators -> in iPad
z = "amazing"
present = "a" in z
print(present)
prs = "a" not in z
print(prs)


ko = "I am learning python programming"
kj = "Python" in ko 
print(kj)
#learning formating tag
age=18
print("My age is " , age)
print(f"My age is{age}")


library = ["Maths" , "Science" , "English"]
lra = "History" in library
print(lra)


a=40
scored = 40
print("Hey this is the final score",(scored>=a))