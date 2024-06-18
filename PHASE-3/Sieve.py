def primeUsingSieve(n):
    isPrime=[True]*(n+1)
    i=2
    while i*i<=n:
        if isPrime[i]:
            for j in range(2*i,n+1,i):
                isPrime[j]=False
        i+=1
    primes=[]
    for i in range(2,n+1):
        if isPrime[i]:
            primes.append(i)

    return primes


n=int(input("Enter the Range to return Prime Numbers :: "))
print(*primeUsingSieve(n))

