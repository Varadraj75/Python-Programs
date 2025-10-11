li=[-6,-5,2,1,7,9]
l=[-1,0,2,4,5,6]

res=[]
left =0
right = len(li)-1
for i in range(len(li)):
    if(li[left]<l[left]):
        res.append(l[left])
        left +=1
    else:
        res.append(li[left])

print(res)
