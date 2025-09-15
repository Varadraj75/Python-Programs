#multiplication Table 

number = int(input("Enter the number between 1 to 10 "))

if(number>= 1 and number<=10):
    for i in range(1,11):
        print(f"{number}x{i}={number*i}")
else:
    print("Enter a valid number between 1 to 10 ")
