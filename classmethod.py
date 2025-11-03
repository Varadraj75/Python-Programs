# class methods = allow operations related to the class itself
#take (cls) as the first parameter , which represents the class itself
#Instance method = best for operations on instances of the class (objects)
# static method = best for utility function that do not need access to class data
# Class method = Best for class-level data or require access to the class itself

class student:
    count=0
    totalgpa=0
    def __init__(self,Name,gpa):
        self.name = Name
        self.gpa = gpa
        student.count +=1
        student.totalgpa += gpa
    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.gpa}"
    #class method
    @classmethod
    def get_count(cls):
        return f"Total no of students; {cls.count}"
    @classmethod
    def get_avg(cls):
        if(cls.count==0):
            return 0
        else:
            return f"{cls.totalgpa/cls.count:.2f}"

student1 = student("varad",10)
student2 = student("patric",1)
student3 = student("sandy",9)
print(student.get_count())
print(student.get_avg())