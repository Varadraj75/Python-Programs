# HCF -> Highest Common Factor 

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))

st1 = set()
st2 = set()

for i in range(1, a+1):
    if a % i == 0:
        st1.add(i)

for j in range(1, b+1):
    if b % j == 0:
        st2.add(j)

result = max(st1 & st2)
print("HCF:", result)


# different approach
n1 = 12
n2 = 18

min_value=min(n1,n2)

for i in range(1,min_value+1):
    if(n1%i==0) and (n2%i==0):
        res = i

print(res)