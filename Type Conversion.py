# Type Coversion (int , float , bool , str , character )

#type()

#assignment
x=200
print(type(x))

#reassignment
x=200.00
print(type(x))

#reassignment 
x="hey this is me"
print(type(x))

#reassignment 
x='@@#4'
print(type(x))

#reassignment
x=True
print(type(x))


#Conversion
# we can't convert the data type from 1 type to the 3rd type for example
# x="10.2"
# y=int(x)
# print(y)
# print(type(y))

#implicit Conversion:  (this is a type in which interpreter do it automatically)
x=5
print(type(x))
x=5+6.324
print(type(x))

x="rahul"+"5"
print(type(x))


#Explicit Conversion: int(),float(),str(),bool()
x=int(5.8)
print(x)
x=x+5.8
print(x)
print(type(x))
x=str(x) + str("+") +str(93.2)
print(x)
print(type(x))
# any value other than 0 will give the result as true
x=bool(x)
print(x)



print(int(9.9))
print(float(True)) #converting boolean to float so in bool true is known as 1.0
print(str(123)+"abc")

#printing in the same line 
print(int(9.9) , float(True) , str(123)+"abc")

x=17+1
print("My name is Varad I am" , x , "year old" )

#string formating 
# by using f in the start and using the {} brackets we can use it 
print(f"my name is varad and i am {x} year old")


# real and imaginary part 

z=3+4j
x= z.imag
k = z.real
print(x)
print(k)