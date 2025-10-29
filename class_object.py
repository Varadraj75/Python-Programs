class student:
    #attributes
    roll_no =0
    name=""
    age=""
    gender=""
    #method 1
    #self refers to the current instance of the class
    def display_info(self):
        print(self.name , self.roll_no,self.age,self.gender)
    #method 2
    def set_info(self):
        self.name = input("Enter the student name")
        self.roll_no = input("Enter the Roll Number")
        self.age = input("Enter the Age")
        self.gender = input("Enter the gender")

s1 = student()


s1.set_info()
s1.display_info()

