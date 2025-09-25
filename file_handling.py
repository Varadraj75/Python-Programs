f = open('demo.txt','r')
data = f.read()
print(data)

i = open(r"/Users/varad/Documents/GitHub/Python-Programs/demo.txt" , 'r')
# readline will read the single line
print(i.readline(1))
print(i.readline(5))
print(i.readline())
# readlines will read all the lines , it creates the list
print(f.readlines())



