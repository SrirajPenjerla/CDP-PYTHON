
num=int(input("enter a number :"))

print("Numbers")
count=0
sum=0
mul=1
while(num>0):
    count=count+1 # 2 number of digits in the number 
    temp=num%10
    sum=sum+temp # 3 sum of digits
    mul=mul*temp # 4 multiplication of digits 
    print(temp)  # 1 printing the digits 
    num=num//10

print("no of digits :" , count )
print("sum of digits: ", sum)
print("mul of digits in the number : ",mul)
