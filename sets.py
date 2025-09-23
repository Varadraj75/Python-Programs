# Sets:- unordered collection of unique elements , it is mutable , No duplicates-> automatically
# removed duplicate values , fast membership testing , holds unique elements , elements must be 
# hashable , mathematical set operation(union , intersection , etc.)


# if there is no elements inside the curly brackets {} then interpreter will asume it to be dictionary.
#Creating a set:
my_set = {1,2,3,2,3,4}
print(my_set)

# Creating an Empty Set:
my_set_2 = set()
print(my_set_2)

#Type of my Set:
print(type(my_set_2))

# Sets of strings
set_strings={'Ferrari' , 'Maruti' , 'RangeRover' , 'Omni Van' ,'Rolling'}
print(set_strings)

# Set from a list:
set_from_list = set([1,2,3,2,3,2,3,23])
print(set_from_list)

#Set from the string:
set_from_string= set(["Varad"])
print(set_from_string)

# add a single number instide the set: .add()
my_set.add(5)
print(my_set)

# Add multiple elements in the set 
my_set.update(["Varad","2007"])
print(my_set)

#Remove the element from the set : .remove() method!
my_set.remove(2)
print(my_set)

# Discard :- removes the element passed: do not give error if key is not ther 
my_set.discard('591')
print(my_set)

# pop(): removes the arbitrary element from the set
my_set.pop()
print(my_set)

#clear() : remove all the elements from the set
my_set.clear()
print(my_set)
my_set.add(0)
#Membership operator in set: in , not in : relatively efficient (faster)
print(0 in my_set)
print(0 not in my_set)

# Calculating the size of the set: len()
print(len(my_set))

for item in my_set:
    print(item, end=" ")


#Set operation:
# 1. Union of the set:- 
set1 = {1,2,3,4,5,}
set2={2,3,6,43,7,5}
print(set1.union(set2))
# 2. Intersection: gives common elements in setA and setB 
print(set1.intersection(set2))

# 3. Difference operation: elements which are in A but not in B. 
print(set1.difference(set2))
print(set2.difference(set1))

#4. Symmetric Difference: gives me the elements present in either set1 or set2 but not in both
print(set1.symmetric_difference(set2))
print(set1^set2)

#5 Subset: checks if all elements of set1 are present in set2
print(set1.issubset(set2))

#6. Superset:
print(set1.issuperset(set2))

#7. Disjoint set:
set3 = {1,2,3,4}
set4={5,6,7,8}
print(set3.isdisjoint(set4))
print(set1.isdisjoint(set2))

#8. Creating a copy of the set: 
new_set = set3.copy()
print(new_set)

#9. Create a set of squares of numbers from 1 to 10 
set6=set()
for i in range(1,11):
    set6.add(i*i)
print(set6)

set7={i*i for i in range(1,11)}
print(set7)

# Create a set of square root of numbers from 1 to 100 and print it
set8={i**0.5 for i in range(1,101)}
print(set8)

# Create a set of even numbers from 1 to 100 
set9={i for i in range(1,101) if(i%2==0)}
print(set9)

# Create a set of odd numbers from 1 to 100 
set10={i for i in range(1,101) if(i%2!=0)}
print(set10)

# Set comprehension using iterable
# Create a set from a string "Hello World" which contains only vowels. 
s ="Hello World"
vowels = "aeiouAEIOU"
set11 = set()
for char in s:
    if char in vowels:
        set11.add(char)
print(set11)

set12 = {char for char in s if char in vowels}
print(set12)

#frozen set:- 
fronzen_empty_set = frozenset() # it creates an immutable version of an empty set
print(fronzen_empty_set)
# set 13 is the immutable version of set 10 
set13 = frozenset(set10)
print(set13)


# Create a set of odd numbers present in the below list  using set comprehension
l=[1,2,3,4,5,6,7,8,12,134]
set1000 = set(l)
set100 = {i for i in range(len(set1000)) if(i%2!=0)}
setodd={i**1/2 for i in range(len(set100))}
print(set100)
print(setodd)


# create a list of  N space separated integers , and find the duplicate elements in it and print the list of duplicate elements 
n = int(input("Enter the input "))
lset = list()
num = 0
dup=[]
for i in range(n):
    num = int(input())
    lset.append(num)

for i in range(len(lset)):
    for j in range(i+1 , len(lset)):
        if lset[i] == lset[j] and lset[i] not in dup:
            dup.append(lset[i])

print(dup)