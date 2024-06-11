def countArray(lis):
    maxele=max(lis)
    arr=[0]*(maxele+1)
    for i in lis:
        arr[i]+=1
    print(arr)
    for i in range(maxele+1):
        if arr[i]!=0 and arr[i] == 1:
            print(i,end=" ")
        elif arr[i]!=0 and arr[i]>1:
            for j in range(arr[i]):
                print(i,end=" ")
    
lis=list(map(int,input().split()))
countArray(lis)