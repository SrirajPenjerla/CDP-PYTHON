def SM(lis,sum):
    if lis:
        sum+=lis[-1]
        return SM(lis[:-1],sum)
    return sum

def Ma(lis,m):
    print(lis)
    if lis and lis[-1]>m:
        m=lis[-1]
        return Ma(lis[:-1],m)
    return m

def Mi(lis,m):
    if lis and lis[-1]<m:
        m=lis[-1]
        return Mi(lis[:-1],m)
    return m

def SU(i,lis):
    if i>=len(lis):
        return 0
    return lis[i]+SU(i+1,lis)


def vowel_str(n,st):
    if n == len(st):
        return ""
    if st[n] in "AEIOUaeiou":
        return st[n]+vowel_str(n+1,st)
    return vowel_str(n+1,st)

st=input()
print(vowel_str(0,st))
# print(SM([15,10,-5,81],0))
# print(Ma([8,7,6,5],float("-inf")))
# print(Mi([15,10,-5,81],float('inf')))
# print(SU(0,[15,10,-5,81]))