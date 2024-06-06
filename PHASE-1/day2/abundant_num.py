# TAKE A NUM INPUT FROM USER CHECK IF  THE SUM OF FACTORS OF THE NUMBER IS GreATER THAN THE ORGINAL NUM IF YES 
# PRINT YES IF NO PRINT NO 

num=int(input("Enter the number "))
sum=0
for i in range(1,num//2+1):
    if num% i == 0:
        print(i,end=" ")
        sum=sum+i
if sum> num:
    print("abundant num")
else:
    print("not abundant")
    
