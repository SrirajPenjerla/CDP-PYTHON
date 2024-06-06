# BUbble sort
arr=[287,232,11,232,11]
for i in range(len(arr)):
    for j in range(len(arr)-i-1):
        if arr[j] > arr[j+1]:
            temp=arr[j]
            arr[j]= arr[j+1]
            arr[j+1]=temp

print(arr)