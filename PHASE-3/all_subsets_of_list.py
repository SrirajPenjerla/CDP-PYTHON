def all_posible(lis,ans,n):
    if n == len(lis):
        print(ans)
        return
    # print(ans)
    all_posible(lis,ans+[lis[n]],n+1)
    all_posible(lis,ans,n+1)
    

    # or
    # ans.append(lis[n])
    # all_posible(lis,ans,n+1)
    # ans.pop()
    # all_posible(lis,ans,n+1)
all_posible([1,2,3,4],ans=[],n=0)

