# program for printing pattern
#              *
#           *  *
#        *  *  *
#     *  *  *  *
#  *  *  *  *  *

n=int(input("Enter number of rowa :"))

for i in range(1,n+1):
    #spaces
    for s in range(1,n-i+1):
        print("   ",end="")
    #pattern 
    for j in range(1,i+1):
        print(" * ",end="")
    print()