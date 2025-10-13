li=[1,2,3,4]
l=[1,23,45,78]
left =0
right = 0 
res = []
n = len(li)
m = len(l)

while(left<n and right<m):
    if(li[left]<l[right]):
        res.append(li[left])
        left +=1
    else:
        res.append(l[right])
        right +=1
    
while(left<n):
    res.append(li[left])
    left +=1

while(right<m):
    res.append(l[right])
    right +=1


print(res)

