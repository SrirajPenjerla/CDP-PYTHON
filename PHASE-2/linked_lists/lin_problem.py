class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

def insert_atbeg(data,head):
    new=Node(data)
    new.next=head
    head.prev=new
    head=new
    return head

def dele(d,head):
    temp=head
    while head!= None:
        # print(head.data)
        if head.next.data == d:
            break
        head=head.next
    head.next.next.prev=head
    head.next=head.next.next
    
    return temp

def make_double_linked_list(arr):
    head=Node(arr[0])
    for i in range(1,len(arr)):
        head=insert_atend(arr[i],head)
    return head

def insert_atend(data,head):
    temp=head
    new=Node(data)
    while head.next != None:
        head=head.next
    head.next=new
    new.prev=head
    return temp

def dis(head):
    temp=head
    while temp!=None:
        print(temp.data,end=" ")
        temp=temp.next
    print()

def dis_rev(head):
    temp=head
    while temp.next!=None:
        temp=temp.next
    while temp!=None:
        print(temp.data,end=" ")
        temp=temp.prev
    print()

def del_ii(head,skip,n):
    temp=head
    count=0
    c2=0
    while count<skip:
        count+=1
        head=head.next
    tem=head.prev
    while c2<n:
        c2+=1
        head=head.next
    if head == None:
        tem.next=head
    else:
        tem.next = head
        head.prev=tem
    return temp

# def del_ii(head,skip,n):
#     temp=head
#     count=0
#     c2=0
#     while temp!=None:
#         if count == skip:
#             tem=temp.next
#         if c2 == (skip+n):
#             break
#         temp=temp.next
#     tem.next=temp
#     temp.prev=tem
#     return temp

head=make_double_linked_list([12,223,44,232,11])
dis(head)
print("after operations::")
head=insert_atbeg(22,head)
head=insert_atend(420,head)
dis(head)
head=dele(223,head)
dis(head)
dis_rev(head)

head=del_ii(head,3,3)
dis(head)
dis_rev(head)
