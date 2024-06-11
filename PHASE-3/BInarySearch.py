def binary(start,end,nums,k):
    if start>end:
        return False
    mid = (start+end)//2
    if nums[mid] == k:
        return mid 
    elif k > nums[mid]:
        return binary(mid+1,end,nums,k)
    else:
        return binary(start,mid-1,nums,k)


nums=list(map(int,input().split()))
k=int(input("Enter element to search :: "))

ans =binary(0,len(nums)-1,nums,k)
if ans:
    print(f"element '{k}' present at {ans} th index")
else:
    print("element Not Found In the list")