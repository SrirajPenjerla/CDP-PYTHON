def bin_str(n,k,s):
    if n == k:
        print(s)
        return 
    bin_str(n+1,k,s+"0")
    bin_str(n+1,k,s+"1")

# bin_str(0,10,"")


def print_even(lis,i,s):
    if i == len(lis):
        return s
    if lis[i]% 5 == 0:
        s+=lis[i]
    return print_even(lis,i+1,s)
print(print_even([4,23,11,22,55,32,90],0,0))