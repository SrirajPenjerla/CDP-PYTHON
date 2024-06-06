arr=[1,3,6,7,9,5,2]
# arr=[3,7,4,4,2,3,5]
# arr=[23,423,1232,34334,221,112,34234]
# arr=[2326354726,423,123223,34223,112,34234]

# find the peak element where the left and right ele are small
def ser(arr):
    s=0
    e=len(arr)-1
    mid=s+(e-s)//2
    peak=0
    while s<=e:
        if arr[mid]>peak and arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            peak=arr[mid]
            break
        elif arr[mid]>arr[mid-1]:
            s=mid+1
        else:
            e=mid-1
        mid=s+(e-s)//2
    print(peak)

ser(arr)
#SOME WHAT DIFF LOGIC
def ser(arr):
    s=0
    e=len(arr)-1
    mid=s+(e-s)//2
    peak=0
    while s<=e:
        if arr[mid]>peak and arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
            peak=arr[mid]
            break
        elif arr[mid-1]>arr[mid]:
            e=mid
        elif arr[mid]<arr[mid+1]:
            s=mid
        mid=s+(e-s)//2
    print(peak)

ser(arr)