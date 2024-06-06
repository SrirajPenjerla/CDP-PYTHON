num=int(input("Enter a number ::"))
count=0
for i in range(2,num/2):
    if num%i==0:
        count=1
        break
if count == 0:
    print("prime")
else :
    print("not a prime")


# if num % 2 == 0 or num%3==0:
#     print("not prime")
# else:
#     print("prime")