# Constructor-> 
# Constructor is a method which will be called when object is created
#types of constuctor->
# Default constructor and parameter constructor
class classplus:
    #attribute
    brand_color="blue"
    
    #defining constructor -> method-constructor
    def __init__(self,company,color="white"):
        print(f"The company color for {company} is {color}")
    

pst=classplus("pst","Yellow")
testbook = classplus("testbook","blue")

class student:
    #constructor
    def __init__(self,n,r,a,g):
        self.name = n
        self.roll_no = r
        self.age = a
        self.gender = g

    #method 1:
    def display_info(self):
        print(self.name,self.roll_no,self.age,self.gender)

#main
s1 = student("kp","4cse04",23,"male")
s1.display_info()

s2 = student("k","4e04",2,"female")
s2.display_info()