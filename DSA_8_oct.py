# t=int(input())
# for i in range(0,t):

#     n= int(input())
#     li = list(map(int,input().split()))

#     set_n = set()
#     res=[]

#     for ele in li:
#         if ele not in set_n:
#             set_n.add(ele)
#             res.append(ele)

# print(len(res))

# for ele in res:
#     print(ele,end=" ")
# print()

t = int(input())
for i in range(t):
    n = int(input())
    li = list(map(int, input().split()))

    set_n = set()
    res = []

    for ele in li:
        if ele not in set_n:
            set_n.add(ele)
            res.append(ele)

    print(len(res))
    for ele in res:
        print(ele, end=" ")
    print()
