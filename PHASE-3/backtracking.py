def valid_parathis(n,s,c1,c2):
    if c2>c1:
        return
    if c1>n//2 or c2>n//2:
        return
    if n == len(s) : 
        print(s)
        return
    valid_parathis(n,s+"(",c1+1,c2)
    valid_parathis(n,s+")",c1,c2+1)

n=int(input("Enter : :  "))
if n % 2 !=0:
    print("NO valid parathesis")
valid_parathis(n,"",0,0)