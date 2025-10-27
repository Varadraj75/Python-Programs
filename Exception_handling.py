#Exception handling 
# code 1:-
# while True:
   

#     try:
#         a=int(input())
#         b=int(input())
#         res = a/b
#     # except ZeroDivisionError:
#     #     print("Please don't give the value 0 to denominator")
#         # continue
#     except Exception:
#         print("Some error")
#     else:
#         print(res)
#     finally:
#         print("my code is running well")


#Code 2:

# try:
#     a={
#             "a":1,
#             "b":2
#      }
#     val=a["c"]
    
# except NameError:
#     print("pls enter valid key name")
# except KeyError:
#     print("Pls enter the exisiting key name in dictionary")
# except Exception:
#     print("sone other error")
# else:
#     print(val)


# code 3: using lists
try:
    li=[1,2,4]
    print(li[3])
    print(li[2]+"hello")
except IndexError:
    print("It is indexError")
except TypeError:
    print("it is an TypeError")

