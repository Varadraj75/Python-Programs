# reverse the number

rev_n = 0 
n = int(input("The number "))
ar = n
while n!=0:
    rev_n = rev_n*10 + n%10
    n //= 10

print(rev_n)

if(rev_n == ar):
    print("It is a palindrome number")
else:
    print("Not a palindrome number")

