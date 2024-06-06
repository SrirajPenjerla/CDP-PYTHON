#wirte the code of armstrong using recursion
def count(num):
    if num==0:
        return 0    
    return 1+count(num//10)

def armstrong(num):
    if num == 0:
        return 0
    return (((num%10)**c)+armstrong(num//10))

num=int(input("Enter the number :: "))
c=count(num)
if num==armstrong(num):
    print("Armstrong number ")
else:
    print('Not an armstrong number')

