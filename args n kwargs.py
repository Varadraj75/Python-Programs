# Args & kwargs function 

# args-> it is a special variable it will take all positional arguments 
# syntax ->  *args
def cal_sum(*args):
    print(args) # format will be tuple 
    print(sum(args)) 


cal_sum(10,20,30,40,60,200)

#kwargs 
# synatx -> **kwargs

def f_n(k,l,**kwargs):
    print(kwargs) # format will be dictionary 

f_n(100,200,a=10,b=20,c=90,d=85,e=324,f=234)