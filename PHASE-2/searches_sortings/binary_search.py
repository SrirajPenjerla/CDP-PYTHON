l=[12,23,34,45,56,78,99]
s=0
e=len(l)-1
# mid=(s+e)//2
t=67
mid=s+(e-s)//2
while (s<=e):
    if l[mid]==t:
        print("element found at ",mid)
        break
    elif t<l[mid]:
        e=mid-1
    elif t>l[mid]:
        s=mid+1
    # elif s == e :
    #     print("Element not found")
    mid=s+(e-s)//2