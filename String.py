# Learning Strings
# Strings are immutable , means we can't change anything

#indexing
school ="polaris"
print(school[2])
print(school[0])
print(school[5])

#Concatenation:

print("Raman" +"Bhari"+" 2")
#print("Raman" +"Bhari"+2) # TypeError


#Slicing:
s = "Aryanlovestoclimbthetree"
w = s[2] + s[3]

print(w)
w = s[2:12]
print(w)
w=""
for i in range(2,10):
    w += s[i]

print(w)

w=s[2:] # from 2 to last index , it will print
print(w)



#split()
print("Aryan-Kumar".split('-')) # it will split the name 


#Q1:- 
s="DataScienceIsFun"

print(s[0]+s[4]+s[15])
#Negative indexing 
print(s[-16],s[-12],s[-1])
print(s[4:11])
print(s[13:16])
#Reverse the string
print(s[::-1])

#len(s) is used to fidn the length of string s. 
p=""
#Reverse using for loop
for i in range(len(s)-1 , -1,-1):
    print(s[i],end="")


