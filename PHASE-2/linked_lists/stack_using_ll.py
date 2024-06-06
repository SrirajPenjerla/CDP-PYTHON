class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def dis(head):
    temp=head
    while temp!=None:
        print(temp.data,end=" ")
        temp=temp.next
    print()

def push(data,head):
    new=Node(data)
    new.next=head
    head=new
    return head

def pop(head):
    ans=head.data
    head=head.next
    return ans

head=Node(12)
head=push(114,head)
head=push(12,head)
head=push(133,head)
head=push(123,head)

# print(pop(head))
dis(head)

