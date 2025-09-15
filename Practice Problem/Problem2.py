# FizzBuzz Variation
# Description:
# Print numbers from 1 to 50 using a for loop:
# If a number is divisible by 3, print "Fizz".
# If divisible by 5, print "Buzz"
# If divisible by both 3 and 5, print "FizzBuzz".
# Otherwise, print the number itself.


for i in range(1,51):
    if(i%3==0):
        print("Frizz")
    elif(i%5==0):
        print("Buzz")
    elif(i%3==0 and i%5==0):
        print("FrizzBuzz")
    else:
        print(i)
    