# Pattern 1:-
for i in range(6):
    print("*" * i)


# Pattern 2:-
n=5
for i in range(1,6):
    space = " " * (n-i)
    star = " *" * i

    print(space + star)