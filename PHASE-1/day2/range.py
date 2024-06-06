#  calulate the diff of sum of numbrs that are divsible by  6 and not by 6 in the range of first 30 num
n=int(input("enter the number :: "))
sum1=0
sum2=0
i=0
while(i<=n):
    if i%6 == 0:
        sum1+=i
    else:
        sum2+=i 
    i=i+1

print(abs(sum1-sum2))