# write a recursive program to print the digits of number in rev order 
def rev(num):
    if num==0:
        return    
    print(num%10)
    return rev(num//10)

n=int(input("Enter the number :: "))
rev(n)