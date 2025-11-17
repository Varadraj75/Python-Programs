n=678
sum=0
while n!=0:
    remainder = n%10
    sum += remainder
    n=n//10

print(sum)

n=678
sum=0
while (n!=0) or (sum>=10):
    if(n==0):
        n=sum
        sum=0
    remainder = n%10
    sum += remainder
    n=n//10

print("The sum value is", sum)