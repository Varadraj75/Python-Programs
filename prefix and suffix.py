# using prefix and post logic (check in iPad page 7-8)

# Using prefix logic out here:
# Method 1
li=[1,2,3,4,5,6,7]
n=len(li)
p_sum =[]
sum=0
for ele in li:
    sum += ele
    p_sum.append(sum)
print(p_sum)

# Method 2
n=len(li)
p1_sum=[0]*n
p1_sum[0]=li[0]
for i in range(1,n):
    p1_sum[i]=p_sum[i-1] + li[i]
print(p1_sum)

#Suffix method logic out here:
#Method 1:
suff_sum=[]
sum=0
suff_sum =[0]*n
# to iterate the loop from the back , iterating the loop from the reverse
for j in range(n-1,-1,-1):
    suff_sum[j]= suff_sum[j-(n-1)] +li[j]
print(suff_sum)

#method 2:
s_sum=[]
sum=0
for j in range(n-1,-1,-1):
    sum = sum + li[j]
    s_sum.insert(0,sum)
print(s_sum)