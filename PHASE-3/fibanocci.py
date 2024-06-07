def fibanocci_using_rec(n):
    if n  == 2:
        return 1
    if n == 1:
        return 1
    return fibanocci_using_rec(n-1)+fibanocci_using_rec(n-2)

# print(fibanocci_using_rec(4))


"""
:::DYANAMIC PROGRAMMING::: 
To reduce the time complexity we store the already calculated sub problem values into a array called as cache this
recursion + cache is called as memoization - Top Down approach
only using cache is called as tabulation - Bottom up approach

"""



# using memoization

def fibanocci_using_memoization(n,cache):
    if n == 1 or n == 2:
        return 1
    elif cache[n]!= -1:
        return cache[n]
    
    res1=fibanocci_using_memoization(n-1,cache)
    res2=fibanocci_using_memoization(n-2,cache)
    cache[n] = res1+res2
    return res1+res2
# n=int(input())
# cache=[-1]*(n+1)
# print(fibanocci_using_memoization(n,cache))


def fib_using_tabulation(n):
    cache = [-1] * (n+1)
    cache[1] =1
    cache[2] = 1

    for index in range(3,n+1):
        r1=cache[index-1]
        r2=cache[index-2]
        cache[index] = r1+r2
    return cache[n]

n=int(input())
print(fib_using_tabulation(n))
