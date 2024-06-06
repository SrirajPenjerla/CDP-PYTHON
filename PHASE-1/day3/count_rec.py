# write a recuersive func to count the num of digits off a num
def c(num):
    if num==0:
        return 0    
    return 1+c(num//10)
n=int(input("Enter the number :: "))
print("total digits::",c(n))