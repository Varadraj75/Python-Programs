# Conditional Statements -> 

#if-else :
"""
if(condition):
    "pass"
else:
    "fail"
"""

#multiple if-else condition
"""
if-elif-else:
if(condition-1):
   #write something
elif(condition-2):
   #write something
elif(condition-3):
  #write something
.
.
.
 else:
 print(condition)
"""


#given the number N , you are supposed to print "yes" or "no " based on the fact wheather it is even or odd.

N = int(input("Enter a value "))
if(N%2==0):
    print("The number is even")
else:
    print("The number is odd")


# Q2:- comparing two match scores

team_a= 200
team_b = 210

if(team_b>team_a):
    print("Team B won the match")
elif(team_b==team_a):
    print("The match has been draw")
else:
    print("Team A won the match")


#Q3:- simple login system 
stored_username = "admin"
entered_username = str(input("Enter the username "))
entered_username = entered_username.strip()

if(stored_username == entered_username):
    print("Login Successful")
else:
    print("Login Failed")


#Q4:- Meal plan recommendation based on age 

age = input("Enter your age")
age = int(age)

if(age>=0 and age<=3):
    print("Recommended Meal Plan : Toddler Meal")
elif(age>=4 and age<=12):
    print("Recommended Meal Plan : kids Meal")
elif(age>=13 and age<=19):
    print("Recommended Meal Plan : Teen Meal")
elif(age>=20 and age<=59):
    print("Recommended Meal Plan : Adult Meal")

#Q4:- movie ticket pricing 
age = int(input("Enter the age "))
if(age>=0 and age<=12):
    print("The movie ticket pricing is just $5")
elif(age>=13 and age<=64):
    print("The movie ticket pricing is just $6")
else:
    print("Senior ticket is priced at just $7")

#Q5:- Pet Age Classification

puppy_age = int(input("Enter the age of the pet"))
if(puppy_age<=1):
    print("Puppy")
elif(puppy_age>=1 and puppy_age<3):
    print("Young Adult")
elif(puppy_age>=3 and puppy_age<8):
    print("mature adult")
elif(puppy_age>=8):
    print("senior")