# LCM stands for least common multiple 

n1=6
n2=5

max_num = max(n1,n2)

mul = max_num

while True:
    if(mul%n1==0 and mul%n2==0):
        ans = mul 
        break

    mul = mul + max_num

print(ans)

# Another approach 




