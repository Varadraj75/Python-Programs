# 1.compile Time.( overloading)
# 2.run time ( overriding)


# def add(a,b):
#     print("function 1")
#     return a+b

# class SBI:
#     def interest(k):
#         print("10%")

# class hdfc:
#     def interest(k):
#         print("7%")

# class pbn:
#     def interest(k):
#         print("8%")

# #shows the behavious of duck
# def show_int(item):
#     item.interest()


# b1=SBI()
# b2=hdfc()
# b3=pbn()
# show_int(b1)
# show_int(b2)
# show_int(b3)



# class student_marks:
     
#      def __init__(self,m):
#             self.mark=m
   
#      def __add__(f,s):
#           return  f.mark+s.mark
     
#      def __sub__(f,s):
#           return  f.mark-s.mark
     
    
#     # user
#      def  __str__(self):
#       return f"student has marks:{self.mark}"
     
#      #developer-much detailed infomration
#      def  __repr__(self):
#       return f"student has attribute mark and value is :{self.mark}"
     
      
           
      
    


# s1=student_marks(100)
# s2=student_marks(200)


# print(s1-s2)
# print(s1)
# print(repr(s1))



class vehicle:
    def __init__(self,p):
        self.price=p

    def start(self):
        print("start logic")

    def stop(self):
        print("stop logic")

class petrol(vehicle):
    def __init__(self, pr,tc):
        super().__init__(pr)
        self.tank_capacity=tc
        
class electric(vehicle):
    def __init__(self, pr,b_c):
        super().__init__(pr)
        self.battery_capacity=b_c


class special_v(petrol,electric):
    def __init__(self,p,tc,bc):
        
        petrol.__init__(tc,p)
        electric.__init__(bc,p)

       
obj=special_v("1000000","5l","200kwh")
        

