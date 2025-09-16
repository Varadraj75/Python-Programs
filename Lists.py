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