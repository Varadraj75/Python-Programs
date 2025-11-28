# bubble sort 

arr = [3,9,1,2,29,20]

n = len(arr)

for i in range(0,n):
    for j in range(0,n-1-i):
        if(arr[j]>arr[j+1]):
            # temp = arr[j]
            # arr[j]=arr[j+1]
            # arr[j+1]=temp
            arr[j],arr[j+1] = arr[j+1],arr[j]
            
        
print(arr)