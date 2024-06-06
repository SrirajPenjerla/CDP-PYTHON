class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
head=Node(2)
def dis(head):
    temp=head
    while temp!=None:
        print(temp.data,end=" ")
        temp=temp.next
    print()
def insert_atend(data,head):
    temp=head
    new=Node(data)
    while head.next != None:
        head=head.next
    head.next=new
    return temp
def ss(head):
    temp=head
    a=0
    b=0
    d=0
    while temp!=None:
        if temp.data == 0:
            a+=1
        elif temp.data == 1:
            b+=1
        elif temp.data == 2:
            d+=1
        temp=temp.next
    print(a,b,d)
    temp1=head
    while a!=0:
        temp1.data=0
        temp1=temp1.next
        a-=1
    while b!=0:
        temp1.data=1
        temp1=temp1.next
        b-=1
    while d!=0:
        temp1.data=2
        temp1=temp1.next
        d-=1
    return head


head=insert_atend(1,head)
head=insert_atend(2,head)
head=insert_atend(2,head)
head=insert_atend(0,head)
head=insert_atend(1,head)
head=insert_atend(2,head)
head=insert_atend(0,head)
head=insert_atend(0,head)
head=insert_atend(1,head)
head=insert_atend(1,head)
dis(head)
head=ss(head)
dis(head)

