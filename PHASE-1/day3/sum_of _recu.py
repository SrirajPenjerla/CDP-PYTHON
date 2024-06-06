# wirte a recursive function to calculate sum of digits of num
def sum(num):
    if num==0:
        return 0   
    return num%10+sum(num//10)

n=int(input("Enter the number :: "))
print("Sum of the digits in the number :: ",sum(n))