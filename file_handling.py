f = open('demo.txt','r')
data = f.read()
print(data)

i = open(r"/Users/varad/Documents/GitHub/Python-Programs/demo.txt" , 'r')
# readline will read the single line
print(i.readline(1))
print(i.readline(5))
print(i.readline())
# seek will be helpful for moving the cursor to the index value
i.seek(0)
# readlines will read all the lines , it creates the list
print(f.readlines())

# it's important to close the file so that no one can edit the file 
i.close()




#  w is for writing inside the file , usage for more than one write will overwrite the data
# in write mode :-
#  methods ->  write(), writelines()
j=open("fle.txt",'w')
j.write('welcome to pst \n varad here')
j.write('hi')
# print statement will return the number of characters were wrote 
print(j.write('hi'))
li=['hey','welcome','pst']
j.writelines(li)
j.close()


# a is for append , it will add the content inside the text file
k=open("file.txt",'a')
k.write('welcome to pst \n varad here')
k.write('hi')
k.close()

# read these file with 'with' statement  , as means alas/alternative name
with open('demo.txt','r') as f:
    print(f.read())

with open('fle.txt','w') as f:
    f.write("file handling")

with open('fle.txt','a') as f:
    f.write(" heyy welcome to pst")