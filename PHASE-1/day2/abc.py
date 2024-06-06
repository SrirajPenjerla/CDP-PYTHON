num=int(input("enter the number  :: "))

n1=num
count=0

while(num>0):
    count+=1
    num=num//10
sum=0

while(n1>0):
    c=n1%10
    sum=sum+(c**count)
    count-=1
    n1=n1//10

print("Sum of digits with their powers of their positions :: ",sum)