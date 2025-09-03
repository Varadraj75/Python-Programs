"""
What is an variable?
-> it is a container to store the data 

Data Types ->

primitive Data Types--->
Integers->
Whole Number 
Natural Number 
Negative Number 


Float->
 Real Numbers 
 Rational Numbers 

Char ->'a' , 'b' , 'c' , '{' , '-' , '0'
1 byte

Boolean -> True or false


Non primitive Data types->
1. String: "delhi"
2. list: [1,2,3,"delhi","hello",4.5]
3. Dictionary: {"Raman":24 , "gracy":22}
4. Tuple: (a,b,c)
5. Sets : set()
"""

"""
Naming Variables:
1. No identifiers/keywords can be used for nomination, example are print , if ,else , for while
2. No predefined function names can be used as variables , print() , input() , map(), int()
3. Should not start from numbers 1,2,3,4
4. Can be started with _ but not with other special characters.
5. Internal space not allowed 
6. Case sensitive 


Case notation:
-> Snake_Case : Less_ordinary 
-> camelCase: lessOrdinary
"""

a = 2
b = 2
print(a+b)
print("The sum of the two numbers are:", a+b)

print(5+7)

#Q1:- Create a variable 'age' and store your age in it . print it
age =17
print("Hey my age is",age)

#Q2:- Create a variable 'city' with the value 'delhi' .
city="Delhi"
print(city)

#Q3:- Assign value 100 to variables x,y,z in one line . print them 
x,y,z=100,100,100
print(x,y,z)

#Q4:- Create a variable score =0 . and update it to 10 . print both old and new values
o=0
print("old value",o)
o=10
print("New value" , o)

#Q5:- Calcute the perimeter of a square (side length=6).
sideLength=6
perimeter_of_square = 4 *sideLength
print(perimeter_of_square)

#Q6:- Store the length and width of a rectangle and calculate area (decimals allowed)
length_of_rect=10.2
width_of_rec= 23.24
areaOfRect = length_of_rect * width_of_rec
print(areaOfRect)
#Q7:- covert celsis temp 37.5 to fahrenheit.
celsis_Temp = 37.5
fahrenheit= celsis_Temp * 9/5 +32
print(fahrenheit)
#Q8:- compare two numbers and store the results as a boolean 
az,ay= 10,20
is_a_greater = (az>ay) # true if a is greater than b ,else false and 
print(is_a_greater)

#Q9:- convert fahrenheit 177.77 to celcius 
fahrenh= 177.77
cElius= (fahrenh-32)* 5/9
print(cElius)


#Q10:- calculate Simple intereset , p=100000, rate = 15, time = 1year
principle , rate , time = 100000 , 15 , 1 
simpleInterest = principle*rate*time/100
print(simpleInterest)


#Q11:- Calculate Compound interest , p=100000, rate = 10 , time = 1 year
compoundPrinciple , compoundRate , compoundTime = 100000 , 10 , 1 
compound_interest = compoundPrinciple*pow(1+compoundRate/100, compoundTime) - compoundPrinciple