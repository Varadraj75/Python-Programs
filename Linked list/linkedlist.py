class node:
    def __init__(self,val):
        self.data = val
        self.next = None


node1 = node(5)
node2 = node(1)
node3 = node(4)

node1.next = node2
node2.next = node3

# print(node2.next.data)
# print(node1.next.next.data)

head = node1 
temp = head
while(temp is not None):
    print(f"{temp.data}->",end="")
    temp = temp.next
print("None")