class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

head=Node(30)
sec=Node(40)
t=Node(50)
head.next=sec
sec.next=t
# head=None
# prev=None
# def insert(head=None,data=None):
#     curr=Node(data)
#     curr.next=
#     if head == None:
#         head=curr
#     return head
# head=insert(head,12)
# head=insert(head,13)
# head=insert(head,14)


def dis(head):
    temp=head
    while temp!=None:
        print(temp.data,end=" ")
        temp=temp.next
    print()
    
dis(head)

def insert_atbeg(data,head):
    new=Node(data)
    new.next=head
    head=new
    return head

def insert_atend(data,head):
    temp=head
    new=Node(data)
    while head.next != None:
        head=head.next
    head.next=new
    return temp

def insert_atpos(head,data,pos):
    temp=head
    new=Node(data)
    count=1
    while count!=pos:
        count+=1
        temp=temp.next
    new.next=temp.next
    temp.next= new
    return head

def lent(head):
    temp=head
    count=0
    while temp!=None:
        count+=1
        temp=temp.next
    return count

def print_mid(head):
    count=lent(head)
    pos=count//2
    c=1
    temp=head
    while c!=pos:
        c+=1
        temp=temp.next
    print(temp.data)
    return temp.data

def dele(d,head):
    temp=head
    while head!= None:
        # print(head.data)
        if head.next.data == d:
            break
        head=head.next
    head.next=head.next.next
    # temp.next=None
    return temp

def dele(d,head):
    temp=head
    while head.next!= None:
        # print(head.data)
        if head.next.data == d:
            head.next=head.next.next
        head=head.next
    # head.next=head.next.next
    # temp.next=None
    return temp

def reverse(head):
    temp=head
    prev=None
    while temp!=None:
        next=temp.next
        temp.next=prev
        prev=temp
        temp=next
    return prev

def rev_from_pos (head,pos):
    c=1
    temp=head
    while c!=pos-1:
        c+=1
        temp=temp.next
    ans=temp.next
    a=reverse(ans)
    temp.next=a
    return head
    
def rev_after_every_pos(head,pos):
    temp=head
    prev=None
    c=0
    while temp!=None and c < pos:
        next=temp.next
        temp.next=prev
        prev=temp
        temp=next
        c+=1
    if next != None:
        head.next=rev_after_every_pos(next,pos)
    return prev




print("Before operations ")
dis(head)

head=insert_atbeg(44,head)
head=insert_atend(444,head)
head=insert_atend(144,head)
head=insert_atend(420,head)
head=insert_atpos(head,520,4)
print("After operations ")
dis(head)
print("length of linkedlist  :: ",lent(head))
print("Middle Element :: ",end=" ")
mid=print_mid(head)
print("After operations ")
head=dele(mid,head)
dis(head)
print("After Reversing :: ")
head=reverse(head)
dis(head)

print("After Reversing at Particular Position :: ")
head=rev_after_every_pos(head,3)
dis(head)

