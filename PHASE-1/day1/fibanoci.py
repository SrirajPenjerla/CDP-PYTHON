a=0
b=1
print(a,end=" ")
print(b,end=" ")
for i in range (8):
    temp=a+b
    print(temp,end=" ")
    a=b
    b=temp
