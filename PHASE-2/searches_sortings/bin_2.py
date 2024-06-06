
import time 

# using binary search find the first and last occurance of 4 and 15

# def ser(t,array):

#     while s<=e:
#         if array[mid] == t:
#             first(s,mid,array,t)
#             last(mid,e,array,t)
#             break
#         elif t<array[mid]:
#             e=mid-1
#         elif t> mid:
#             s=mid+1
#         mid=s+(e-s)//2

def first(array,t):
    s=0
    e=len(array)-1
    mid=s+(e-s)//2
    ans=0
    while s<=e:
        if array[mid]==t:
            ans=mid
            e=mid-1
        elif t< array[mid]:
            e=mid-1
        elif t> mid:
            s=mid+1
        mid=s+(e-s)//2
    print("first ocuurance:" ,ans)

        
def last(array,t):
    s=0
    e=len(array)-1
    mid=s+(e-s)//2
    ans=0
    while s<=e:
        if array[mid]==t:
            ans=mid
            s=mid+1
        elif t< array[mid]:
            e=mid-1
        elif t> mid:
            s=mid+1
        mid=s+(e-s)//2
    print("Last ocuurance:" ,ans)
st=time.time()
array=[1,4,4,4,9,13,15,15]
first(array,15)
last(array,15)
et=time.time()
x=st-et
print(x)