#write  A program to accept maths makrks from user and check marks greater than 35 print cheated if marks=35 pass and marks <35 fail

marks=int(input("enter your maths marks ::"))

if marks>35:
    print("cheated")
elif marks==35:
    print('pass')
else:
    print("fail")
