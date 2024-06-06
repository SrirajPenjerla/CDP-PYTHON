l=list(map(int,input("enter array :: ").split()))
n=int(input("Enter element to search :: "))

for i in range(len(l)):
    if l[i]==n:
        print("Element found at ",i,"position")
        break 
    elif i == len(l)-1:
        print("Element not found")