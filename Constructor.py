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