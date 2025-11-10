import random
print(random.random())
print(random.random(50,80))

li=['a','b','c','d']
random.shuffle(li)
print(li)

print(random.choice(li))