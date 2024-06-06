# import time 
# using binary search find the first and last occurance of 4 and 15impoe
def ser(t,array):
    s=0
    e=len(array)-1
    mid=s+(e-s)//2
    while s<=e:
        if array[mid] == t:
            first(s,mid,array,t)
            last(mid,e,array,t)
            break
        elif t<array[mid]:
            e=mid-1
        elif t> mid:
            s=mid+1
        mid=s+(e-s)//2

def first(s,e,array,t):
    ans=0
    mid=s+(e-s)//2
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

        
def last(s,e,array,t):
    ans=0
    mid=s+(e-s)//2
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
# st=time.time()
array=[1,4,4,4,9,13,15,15]
ser(15,array)
# et=time.time()
# x=st-et
# print(x)