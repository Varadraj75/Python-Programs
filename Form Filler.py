# Form Filler:
# user enters name , age , marks -> all strings -> convert appropriately 
# Display a formatted message.


name=str(input("Please enter your name "))
age=int(input("please enter your age "))
marks=float(input("please enter your marks "))


name = str(name)
age = str(age)
marks = str(marks)

print("Name:-",name)
print("Age:-",age)
print("Marks:-",marks)
print("")

# f is the formatting tag.
print(f"Name {name} , Age {age} , Marks {marks}")
#trying to use the boolean concept with the numbers to check the output
print(3+True)