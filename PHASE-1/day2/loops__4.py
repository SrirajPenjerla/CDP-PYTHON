n=int(input("enter rows :"))

for i in range(n):
    for j in range(i):
        print(i,end=" ")
    print()
for i in range(n,0,-1):
    for j in range(0,i):
        print(i,end=" ")
    print()