arr=[1,0,1,2,0,0,3,5]
n=len(arr)
sum=0
for i in range(n):
    if arr[i]!=0 and arr[sum]==0:
        arr[sum],arr[i]=arr[i],arr[sum]
    if arr[sum]!=0:
        sum +=1

print(arr)
