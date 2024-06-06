#aggresive COWS
#angry birds minimun dist should be max
#OPPOSITE OF THIS QUESTION 

def possible(s,pages,mid):
    sum1=0
    ns=1
    for i in range(0,len(pages)):
        if sum1+pages[i]<=mid:
            sum1 += pages[i]
        else:
            ns +=1
            if ns > s or pages[i]>mid:
                return False
            sum1 = pages[i]
    return True

def bins(stu,pages):
    sp=0
    for i in pages:
        sp+=i
    print(sp)
    s=0
    e=sp
    mid=s+(e-s)//2
    print(mid)
    while s<=e:
        if possible(stu,pages,mid):
            ans=mid
            print(ans)
            e = mid-1
        else:
            s = mid+1
        mid=s+(e-s)//2
        print(mid)
    return ans

pages=[10,20,30,40]
print(bins(2,pages))







