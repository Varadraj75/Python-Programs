# learning keywords :- break , continue , pass

   #Break:  it is use to terminate the loop when the condition is true 

# Q1:- keep taking numbers until the user enters 0 , then print sum 
# First approach for this question
num = -1
sum = 0 

while num !=0:
    num = int(input("Enter the value"))
    sum  += num


print(sum)


# Second approach for this question 
sum =0 
while True:
    num = int(input("Enter the value"))
    if(num == 0):
        break
    else:
        sum += num

print(sum)


   # Continue:


#Q2:- Print "I am DOn" whenever a multiple of 3 appears otherwise print "I am pilot"\

n = int(input("Enter the value"))
for i in range(n):
    if i%3==0:
        print("I am don")
        continue
    else:
       print("I am pilot")



#Q3:- reverse a number using while loop 

# Logic :- 34 %10 = 4 
        #. 34/10 = 3
        #.  3%10 = 3
        #.  3/10 = 0
        
n =34
rev = 0
while n !=0:
    rev = n%10
    n = n/10
    
   
print(rev)