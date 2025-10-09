li=[1,2,3,4,5,6]
for i in range(len(li)):
    for j in range(i,len(li)):
        for k in range(i,j+1):
            print(li[k],end=" ")
        print()

print("kaden's algorithm")
li = [1, 2, -3, 4, -1, 2, 1, -5, 4]
curr_sum = 0
max_sum=float('-inf')
for i in range(len(li)):
    curr_sum += li[i]

    if(curr_sum>max_sum):
        max_sum = curr_sum
    
    if(curr_sum<0):
        curr_sum = 0

print(max_sum)

# finding the duplicates 

li=[1,2,21,2,1,2,12,2]
value_set = set()
output=[]

for ele in li:
    if ele in value_set:
        output.append(ele)
    else:
        value_set.add(ele)

print(output)

print(-10%3)