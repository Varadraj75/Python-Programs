#What is lists?
#Lists in python are ordered collections used to store 
# multiple items,s they can be created using square brackets or the list() 
# constructor for flexibility.


l =  list()
print(l)
#append(): list method used to insert/append element at the end of the list.
l.append(4)
l.append(1)
l.append(10)
l.append("Hey this is me varad")
print(l)

l2=[]
l2.append("yo")
l2.append("ygo")
l2.append("yoga")
l2.append(1223)
print(l2)


#Indexing:-
print(l2[1])
print()
#Create a list containing your name , age , school , marks in last assessment and print the elements in the format 
#Name: Varad
#Age: 24
# College:- PST 
#marks :- 500

lis = ["Varad" , "17" ,"PST" , 500]
print(f"Name: {lis[0]}")
print(f"Age: {lis[1]}")
print(f"College: {lis[2]}")
print(f"Marks: {lis[3]}")

print(f"{lis[0]} {lis[1]} {lis[2]} {lis[3]}")

for i in range(0,4):
    print(lis[i] , end=" ")

n = input()


# How to read a list input
# Given read N integers, each integer is given in seperate line 
#Input 
"""
6
1
2
3
4
5
12
"""

#output
"""
27
"""

# n = int(input("Enter the input "))
# lset = list()
# num = 0
# for i in range(n):
#     num = int(input())
#     lset.append(num)

# sum = 0 
# for i in range(n):
#     sum += lset[i]

# print("The sum of the entered numbers are: ",sum)


#List Slicing: list_name[start_index:end_index+1]
# print(lset[1:3])
# print(lset[1:])


#Q2:- Read a list of N integers, then print elements which are present 
# on even position , consider 0 as even position 

n = int(input("Enter the list size"))
los = list()
num = 0 
for i in range(n):
    num = int(input())
    los.append(num)

for i in range(0,n,2):
    print(los[i])

print(los[0:n:2])


#pop():- Removes the last element from the list.
l2.pop()
print(l2)

l3= [10,20,30,40,50,60,10]
l3.pop(4)
print(l3)

# remove():- Removes the first occurence of a particular element you are passing.
l3.remove(20)
print(l3)


# count() :- Counts the number x of elements in the list
print(l3.count(6))

# extend[]:- Extends the list by another list
l3.extend[5,6,7,8]
print(l3)

# sort():- it sorts the list in ascending order.
l3.sort()
print(l3)

#reverse() :- it reverse the list
l3.reverse()

#clear() :-it is use to clear all the elements
l3.clear()
