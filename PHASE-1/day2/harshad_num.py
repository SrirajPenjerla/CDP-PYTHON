# tAKE AN INTEGER AS AN INOUT FROM THE USER AND CHECK WEATHER IF THE NUM IS DIVISIBLE BY SUM OF DIGITS OR NOT 

num=int(input("Enter a number :: "))
temp=num
sum=0
while(num>0):
    c=num%10
    sum=sum+c
    num=num//10

if temp%sum==0:
    print("HARSHAD NUMBER  !!!!")
else:
    print("NOT HARSHAD NUMBER !!!! ")