class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

def make_linked_list(arr):
    head=Node(arr[0])
    for i in range(1,len(arr)):
        head=insert_atend(arr[i],head)
    return head

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

def merger(head1,head2):
    i=head1
    j=head2
    head=Node(0)
    tem=head
    while i!= None and j!=None:
        if i.data <=j.data:
            head.next=i
            i=i.next
        else:
            head.next=j
            j=j.next
        head=head.next
    if i!=None:
        head.next=i
    if j!=None:
        head.next=j
    return tem.next

head1=Node(11)
head2=Node(12)
head1=insert_atend(22,head1)
head1=insert_atend(33,head1)
head2=insert_atend(21,head2)
head2=insert_atend(34,head2)

print("before merging :: ")
dis(head1)
dis(head2)
head=merger(head1,head2)
print("After merging :: ")
dis(head)

print("before merging :: ")
head3=make_linked_list([12,34,112,444])
head4=make_linked_list([0,22,23,45,444,2245])
dis(head3)
dis(head4)
head=merger(head3,head4)
print("After merging :: ")
dis(head)
