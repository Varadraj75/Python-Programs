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