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

print("")
#Q2:- 
l="Hello, Python World!"
print(l[14:19])
for i in range(1,len(l),2):
    print(l[i],end="")

print(l[1::2])
# here 3 is the step size
print(l[1::3])

print(l[7:len(s)-1])


none = "abcdefghij"
print(none[2:5])
print(none[-3:])
print(none[::3])


#find() : it gives me the starting index of the word which we are passing in the original string s. 

s= " Hello world " 
print("finding",s.find('o'))

print(s)
#Strip() : it removes the spaces from the start and the end
print(s.strip())


# Replace function: replace(s,s2) -> it replace the word  , s-> initial word , s2 -> replace word
s2 = s.replace('world','python')
print(s2)
# if u want to replace only one word  add 1 in last
s2 = s.replace('wolrd' , 'python',1)
# if u want to replace only one word  add 2 in last
s2 = s.replace('wolrd' , 'python',2)



#Q3:- 

random="   welcome to,  Python programming. Enjoy Coding!   "
print(random.strip())
print(random.replace(',' , ';'))
print(random.find("Python"))
sp = random.split(" ")
print(len(sp))
print(random.split("."))