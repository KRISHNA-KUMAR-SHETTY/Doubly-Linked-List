#Node class
class Node:
    def __init__(self,val):
        self.val=val
        self.prev=None
        self.next=None


#doubly linked list class and methods

class DLL:

    def __init__(self):
        self.head=None

    def insert_at_beg(self,val):
        new_node= Node(val)
        if self.head is None:
            self.head= new_node
            return
        new_node.next= self.head
        self.head.prev=new_node
        self.head=new_node
        return
    
    def insert_at_mid(self,val,index):
        new_node=Node(val)
        if self.head is None:
            self.head= new_node
            return
        if index==0:
            new_node.next= self.head
            self.head.prev=new_node
            self.head=new_node
            return
        temp=self.head
        i=1
        while i<index and temp.next!=None:
            temp=temp.next
            i+=1
        if temp.next is not None:
            new_node.prev=temp
            new_node.next=temp.next
            temp.next.prev=new_node
        new_node.prev=temp
        temp.next=new_node
        return 
    
    def insert_at_end(self,val):
        new_node=Node(val)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        new_node.prev=temp
        temp.next=new_node
        return

    def traverse(self):
        if self.head is None:
            return "List is empty"
        temp=self.head
        while temp!=None:
            print(temp.val,end=' ')
            temp=temp.next
        print()

    def reverse_traverse(self):
        if self.head is None:
            return "List is empty"
        temp=self.head
        while temp.next!=None:
            temp=temp.next

        while temp is not None:
            print(temp.val,end=' ')
            temp=temp.prev
        print()
 


    


n1= DLL()
n1.insert_at_beg(40)
n1.insert_at_beg(20)
n1.insert_at_mid(30,1)
n1.insert_at_mid(50,6)
n1.insert_at_end(60)
n1.insert_at_beg(10)
n1.traverse()
n1.reverse_traverse()



