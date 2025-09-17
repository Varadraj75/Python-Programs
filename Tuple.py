# A tuple is an ordered, immutable collection of items in Python,
# similar to lists but cannot be modified after creation . 

#Tuples
tpl=()
print(tpl)


#Ordered data types
tpl1 = (1,2,3)
tpl2 = (1,3,2)
print(tpl1 , tpl2)

# it stores Heterogeneous data
tpl3 = 2,3,4,5,6,7.2,"Varad"
print(tpl3)


# Accessing elements in tuples
print(tpl1[0])
print(tpl1[1])
print(tpl1[2])
print(tpl2[0])
print(tpl2[1])
print(tpl2[2])
print(tpl3[-1])

# Immutability:- element stored cannot be changed! but but but...
# we have list in the tuple we can change the list value
tpl6 = 2,3,4,5,6.9,"Varad",[3,4]
print(tpl6)
tpl6[-1][0] = 100
print(tpl6)
l = tpl6[-1]
l[0] = 100
print(l)


#Tuple Concatenation: (+) Used to concatenate tuples in the order they are.
tpl8 = tpl1 +tpl2 
print(tpl8)


#Tuple Multiplication:
print(tpl1*3)

# Tuple Membership: (in, not in)
print(2 in tpl2)
print(2 not in tpl2)

#Iteration:
for item in tpl2:
    print(item,end=" ")


#Count(arg): count the number of times and element appears
print(tpl1.count(2))

# index() : Inorder to find the frst index of a particular element
print(tpl2.index(2))