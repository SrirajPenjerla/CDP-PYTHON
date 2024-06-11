def Linear(k,index,nums):
    if index>=len(nums):
        return False
    if nums[index] ==  k:
        return index
    return Linear(k,index+1,nums)

nums=list(map(int,input().split()))
k=int(input("Enter element to search"))

ans = Linear(k,0,nums)
if ans:
    print(f"element present at {ans} th index")
else:
    print("element Not Found In the list")