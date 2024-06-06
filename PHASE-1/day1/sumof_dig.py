# calc the sum of digits of a num which is taken as input frm usr 
num=int(input("Enter a num ::"))
sum=0
while num>0:
    sum=sum+(num%10)
    num=num//10
print(sum)

