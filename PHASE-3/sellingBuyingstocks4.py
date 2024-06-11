class Solution(object):
    def maxProfit(self, k, prices):
        def solve(index,k,brought):
            if k == 0 or index == len(prices):
                return 0
            maxProfit=0
            if brought == 0:
                buyNow=-prices[index]+solve(index+1,k,1)
                buyLater=solve(index+1,k,0)
                maxProfit=max(buyNow,buyLater)
            else:
                sellNow=prices[index]+solve(index+1,k-1,0)
                sellLater=solve(index+1,k-1,1)
                maxProfit=max(sellNow,sellLater)
            return maxProfit
        cache=[[[0]*2 for _ in range(k+1)] for i in range(len(prices)+1)]
        print(cache)
        def memoization(index,k,brought):
            if k == 0 or index == len(prices):
                return 0
            elif cache[index][k][brought]!=-1:
                return cache[index][k][brought]
            maxProfit=0
            if brought == 0:
                buyNow=-prices[index]+memoization(index+1,k,1)
                buyLater=memoization(index+1,k,0)
                maxProfit=max(buyNow,buyLater)
            else:
                sellNow=prices[index]+memoization(index+1,k-1,0)
                sellLater=memoization(index+1,k,1)
                maxProfit=max(sellNow,sellLater)
            cache[index][k][brought]=maxProfit
            return cache[index][k][brought]

        def tabulation():
            n=len(prices)
            cache=[[[0]*2 for _ in range(k+1)] for i in range(n+1)]
            
            for index in range(n-1,-1,-1):
                for n in range(1,k+1):
                    for brought in range(2):
                        maxProfit=0
                        if brought == 0:
                            buyNow=-prices[index]+cache[index+1][n][1]
                            buyLater=cache[index+1][n][0]
                            maxProfit=max(buyNow,buyLater)
                        else:
                            sellNow=prices[index]+cache[index+1][n-1][0]
                            sellLater=cache[index+1][n][1]
                            maxProfit=max(sellNow,sellLater)
                        cache[index][n][brought]=maxProfit
            print(cache)
            return cache[0][n][0]
        
        return tabulation()
        