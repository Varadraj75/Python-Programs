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


# Retrieving values from disctionaries: name_of_dictionary[key]
print(d3["Name"])

# in Operator is used to check whether a specific "key" exists in the
# dictionary or not. 
# Syntax:- key in my_dict --> T/F depending upon the exsitence of key. 

print("Age" in d3)
print("college" in d3)


