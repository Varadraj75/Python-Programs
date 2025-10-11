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
l=[1,2,3,4,5,6]
curr_sum = 0
max_ele = float('-inf')

for i in range(0,len(l)):
    curr_sum += l[i]

    if(curr_sum>max_ele):
        max_ele=curr_sum
    if(curr_sum<0):
        curr_sum=0

print(max_ele)