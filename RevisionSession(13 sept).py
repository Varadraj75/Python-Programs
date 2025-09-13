# Q1:- A student enters marks for 3 subjects as Strings. convert them to int and calculate the average.

subject_1 = float(input("Enter the maths score"))
subject_2 = float(input("Enter the science score"))
subject_3 = float(input("Enter the computer score"))

subject_1 = int(subject_1)
subject_2 = int(subject_2)
subject_3 = int(subject_3)

avg = subject_1+subject_2+subject_3 / 3

print(avg)


#Q2:- take a number age = 25. convert it into a string and print "My age is 25". 

age = 25
print(f"My age is {age}")


#Q3:- A shopping site shows price as String "499.99". Add delivert charge(50 as int) and print the final bill. 

price = ("499.99")
price = int(float(price))

delivery_charge = price+50

print(f"The final bill is {delivery_charge}")

#Q4:- Take a complex number z=5+2j.
# conver it into string. 
# extract real and imaginary part as int 
# print their sum 

compl = 5+2j
real = int(compl.real)
img = int(compl.imag)

print(real+img)




#Fucntion 
#defining the function
# in these age is the parameter
def isEligible(age):
    # these age is reference of the value , which will be passed when the function is called 
    if(age>=18):
        print("Eligible for voting!")
    else:
        print("Not Eligible for voting!")


age = int(input("Enter the age "))
#calling the function
# in these age is the argument
isEligible(age)

