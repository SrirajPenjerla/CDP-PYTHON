class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def dis(head):
    temp=head
    while temp!=None:
        if temp.next == head:
            print(temp.data,end=" ")
            break
        print(temp.data,end=" ")
        temp=temp.next
    print()

def dis(head):
    temp=head
    while temp!=None or temp==head:
        print(temp.data,end=" ")
        temp=temp.next
    print()

def insert_atend(data,head):
    temp=head
    new=Node(data)
    while head.next!= temp:
        head=head.next
    new.next=temp
    head.next=new
    return temp

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

def make_circle_linked_list(arr):
    head=Node(arr[0])
    head.next=head
    for i in range(1,len(arr)):
        head=insert_atend(arr[i],head) 
    return head

head=make_circle_linked_list([1,22,3,123,1233])
dis(head)