ab = [1,2,3,4,5,6,7,9]

for i in range(1, len(ab)+1):   # start from 1 so slices aren’t empty
    print(ab[0:i])
    print(ab[1:i]) if i > 1 else None
    print(ab[2:i]) if i > 2 else None
    print(ab[3:i]) if i > 3 else None
    print(ab[4:i]) if i > 4 else None
    print(ab[5:i]) if i > 5 else None
    print(ab[6:i]) if i > 6 else None
    print(ab[7:i]) if i > 7 else None
    print(ab[8:i]) if i > 8 else None