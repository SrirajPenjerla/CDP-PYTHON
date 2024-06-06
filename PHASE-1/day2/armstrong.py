num=int(input("Enter the number :"))
temp=num
temp2=num
count=0

while(num>0):
    count+=1
    num=num//10
sum=0
while(temp>0):
    c=temp%10
    sum=sum+(c**count)
    temp=temp//10

if temp2 == sum:
    print(":: Armstrong Number :: ")
else:
    print(":: not armstrong ::")