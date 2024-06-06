n=int(input("enter number of rows :: "))

for i in range(0,n):
    for s in range(0,n-i):
        print("   ",end=" ")
    for j in range(0,2*i-1):
        print(" ₹ ",end=" ")
    print()

for k in range(n,0,-1):
    for l in range(0,n-k):
        print("   ",end=" ")
    for m in range(0,2*k-1):
        print(" ₹ ",end=" ")
    print()