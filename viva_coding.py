# reverse an array
li=[1,2,3,34,4,4]
re =[]
for i in range(len(li)-1,-1,-1):
    re.append(li[i])

print(re)

# finding the duplicates
nums=[1,2,3,5,2,21,1]
value_set = set()
output=[]
for ele in nums:
    if ele in value_set:
        output.append(ele)
    else:
        value_set.add(ele)

print(output)


# find all the subarrays
li=[5,4,-1,7,8]

for i in range(0,len(li)):
    for j in range(i,len(li)):
        for k in range(i,j+1):
            print(li[k],end=" ")
        print()


print("logic here")

# Kadane’s Algorithm - Maximum Subarray Sum
l = [1, 2, 2345, 234, 1, 12, 32, 4, 23, 42, 34, 23, 42, 3]
curr_sum = 0
max_ele = float('-inf')

for i in range(len(l)):
    curr_sum += l[i]

    if curr_sum > max_ele:
        max_ele = curr_sum

    if curr_sum < 0:
        curr_sum = 0

print("Maximum subarray sum =", max_ele)



# Check if an array is a palindrome

arr = [1, 2, 3, 2, 1]  # you can change this list

if arr == arr[::-1]:
    print("The array is a palindrome.")
else:
    print("The array is not a palindrome.")
