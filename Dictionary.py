# Dicitionary :

#Method-1: Creating Dictionaries
d = {"Name" : "Raman" , "Age" : "29" , "COLLEGE" : "PST"}
print(d)

#Method-2 : 
d2 = dict(Name="varad" , Age = 25)
print(d2)

#Method-3:
d3 ={}
d3["Name"] = "Varad"
d3["Age"] = "Hidden"
d3["College"] = "PST"
print(d3)

#iteration over the values
for j in d3.values():
    print(j)

# Retrieving values from disctionaries: name_of_dictionary[key]
print(d3["Name"])

# in Operator is used to check whether a specific "key" exists in the
# dictionary or not. 
# Syntax:- key in my_dict --> T/F depending upon the exsitence of key. 

print("Age" in d3)
print("college" in d3)


#len()-> it is the function to calculate the number of key,value pairs
print(len(d3))


# keys():
print(d3.keys())

for key in d3.keys():
    print(key)


# Items()
print(d3.items())

for (key,value) in d3.items():
    print(key,value)


#update method in dictionary
d3.update({'Balance':0, 'Location':'Bangalore'})
print(d3)

#Nested Dictionaries:
d4 = {'Description':{'Name':'Rahul' , 'Age':21 , 'College':'PST'}}
print(d4)