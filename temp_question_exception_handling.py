try:
    temp = float(input())
    if (temp< -273.15):
        raise ZeroDivisionError("Temperatur below absolute zero is not valid.")
except ZeroDivisionError as a:
    print(a)
except Exception:
    print("An unknown error occurred.")
else:
    print("The celcius temp is",temp)
    far = (temp*9/5)+32
    print("The fa temp is",temp,far)
finally:
    print("Code is working")