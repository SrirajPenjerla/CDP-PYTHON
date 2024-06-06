l=[2,1,2,2,0,1,2,0,0,1,1]
c=0
v=0
b=0
for i in l:

    if i==0:
        c+=1
    elif i==1:
        v+=1
    else :
        b+=1
index=0
while c!=0:
    l[index]=0
    c-=1
    index+=1    
while v!=0:
    l[index]=1
    v-=1
    index+=1
while b!=0:
    l[index]=2
    b-=1
    index+=1
print(l)
#output=[0,0,0,1,1,1,1,2,2,2,2]