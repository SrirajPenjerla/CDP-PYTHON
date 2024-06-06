# shift all the 0s to right with out changing order of remaining numbers
l=[2,0,1024,0,40,230,0]
n=len(l)
l2=[]
for i in range(n):
    if l[i] !=0:
        l2+=[l[i]]
for i in range(n):
    if l[i] == 0:
        l2+=[0]
        

        
        
    
print(l2)