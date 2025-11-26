arr1=[24,41,33,42,17]
n=len(arr1)
for i in range(n-1):
    min=i
    for j in range(i+1,n):
        if arr1[j] < arr1[min]:
            min=j
            arr1[i],arr1[min]=arr1[min],arr1[i]
print("Sorted array is ",arr1)