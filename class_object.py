class student:
    #attributes
    roll_no =0
    name=""
    age=""
    gender=""
    def display_info(self):
        print(self.name , self.roll_no,self.age,self.gender)

s1 = student()
s1.roll_no=10
s1.name="hari"
s1.age=19
s1.gender="male"

#self refers to the current instance of the class



s1.display_info()
