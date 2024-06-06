'''write a program to check the  type of triangle where you take the input from user for 3 sides and classify it accordingly intlo 
equillateral 
scalane 
isoceles'''

a=int(input("enter side 1 :: "))
b=int(input("enter side 2 :: "))
c=int(input("enter side 3 :: "))

if a == b == c:
    print('Equillateral')
elif a == b or b == c or a == c:
    print('isoceles') 
else:
    print('Scalane')
