class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head=None
    def insertathead():
        pass
    def insertatend(self,val):
        newnode = Node(val)
        if(self.head is None):
            self.head = newnode
            return 

        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        
        temp.next = newnode
    def insertatpost():
        pass
    def display(self):
        temp = self.head
        while(temp is not None):
            print(f"{temp.data}->",end="")
            temp = temp.next
        
        print("None")


ll = Linkedlist()

a = int(input("Enter the number you want to enter in the node "))

for i in range(a):
    val = int(input(f"Enter the node{i+1} value"))
    ll.insertatend(val)

ll.display()