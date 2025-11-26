class Node:
    def __init__(self,val):
        self.data = val
        self.next = None
    
class Linkedlist:
    def __init__(self):
        self.head=None
    def insertathead(self,val):
        newnode = Node(val)
        newnode.next=self.head
        self.head = newnode
    def insertatend(self,val):
        newnode = Node(val)
        if(self.head is None):
            self.head = newnode
            return 

        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        
        temp.next = newnode
    def insertatpost(self,val,pos):
        newnode = Node(val)
        if(pos==1):
            self.insertathead(val)
            return
        
        temp = self.head
        count = 1
        while(temp is not None and count<pos-1):
            temp = temp.next
            count += 1
        
        if(temp is None):
            print("Invalid given postion")
            return 
        
        newnode.next = temp.next
        temp.next=newnode
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