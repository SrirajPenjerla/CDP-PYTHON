def can_Jump(curr,n,ans):
    if curr>n:
        return 
    if curr == n:
        print(ans) 
        return 

    can_Jump(curr+1,n,ans+"1")
    can_Jump(curr+2,n,ans+"2")
    

can_Jump(97,100,"")