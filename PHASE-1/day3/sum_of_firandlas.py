# write a func to calc sum of first and last digit of a num 

def sum(num):
    ldigit=num%10
    while (num>0):
        a=num
        num=num//10
    print("Sum of first and last digit of the num ::",a+ldigit)

num=int(input("enter the number :: "))
sum(num)