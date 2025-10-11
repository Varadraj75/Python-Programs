#find the min and max in the array 

li=[10,2,3,4,5]
min_ele = max_ele = li[0]
for ele in li:
    if(min_ele>ele):
        min_ele=ele
    if(ele>max_ele):
        max_ele=ele

print(min_ele)
print(max_ele)


#Find the duplicates in the list 

l=[1,1,2,2,5,2,6,7,5,3,3]

value=set()
output=[]
for ele in l:
    if(ele in value):
        output.append(ele)
    else:
        value.add(ele)

print(output)


#Find all the subarrays:-
for i in range(0,len(l)):
    for j in range(i,len(l)):
        for k in range(i,j+1):
            print(l[k],end=" ")
        print()

#Find the maxsumarray
print("Max-Array")
l=[-1,-1,-2,-5,1,2,5,-10]
curr_sum = 0
max_ele = float('-inf')

for i in range(0,len(l)):
    curr_sum += l[i]

    if(curr_sum>max_ele):
        max_ele=curr_sum
    if(curr_sum<0):
        curr_sum=0

print(max_ele)

#when list has all negative nums 

l = [-2, -3, -1, -4]
curr_ele = max_ele = l[0]

for i in range(1,len(l)):
    curr_ele = max(l[i],curr_ele+l[i])
    max_ele = max(max_ele,curr_ele)
print(max_ele)

#Find the pairs (two sums):
res=[-1,-1]
nums = [1, 2, 3, 4, 5, 6, 7, 7, 8]
target=9

for i in range(0, len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            res[0] = nums[i]
            res[1] = nums[j]
            break # Found the pair, exit inner loop


print(res)

#Finding the intersection
# class Solution(object):
#     def intersection(self, nums1, nums2):
#         """
#         :type nums1: List[int]
#         :type nums2: List[int]
#         :rtype: List[int]
#         """
#         set1=set(nums1)
#         set2 = set(nums2)
#         result = list(set1 & set2 )

#         return result

#Finding the middle index 

li=[1,2,3,4,5,5]
prefix_Sum=0
pre=[]
suffix_sum=0
suf=[]
for ele in li:
    prefix_Sum = prefix_Sum+ele
    pre.append(prefix_Sum)

for i in range(len(li)-1,-1,-1):
    suffix_sum = suffix_sum +li[i]
    suf.insert(0,suffix_sum)

#finding the middle index 
for i in range(0,len(pre)):
    if(pre[i]==suf[i]):
        print(i) 

print(-1)


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


