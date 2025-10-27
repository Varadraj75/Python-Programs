#Exception handling 
while True:
   

    try:
        a=int(input())
        b=int(input())
        res = a/b
    # except ZeroDivisionError:
    #     print("Please don't give the value 0 to denominator")
        # continue
    except Exception:
        print("Some error")
    else:
        print(res)
    finally:
        print("my code is running well")
        