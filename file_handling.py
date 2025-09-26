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


j=open("fle.txt",'w')
j.write('welcome to pst')