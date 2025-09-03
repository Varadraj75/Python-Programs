#Create a simple calculator which takes random values and perform basic arithmentic operation
#like +,-,/,%
# Enter the first number from the user 
# Enter the second number from the user
# The sum of a and b is :
# The Substraction of b from a is:
# The division of a by b is:
# The modulus of a by b is:

#Taking the input from the user
number_1 = int(input("Enter the first Number "))
print(number_1)
number_2= int( input("Enter the secound Number "))
print(number_2)

print(f"The sum of {number_1} and {number_2} is: {number_1 + number_2}")
print(f"The Subtraction of {number_1} and {number_2} is: {number_1 - number_2}")
print(f"The Division of {number_1} and {number_2} is: {number_1 / number_2}")
print(f"The Modulus of {number_1} and {number_2} is: {number_1 % number_2}")


