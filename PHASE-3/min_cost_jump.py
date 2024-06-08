## RECURSION TIME LIMIT EXCEEDS

# class Solution(object):
#     def minCostClimbingStairs(self, cost):
#         n=len(cost)
#         def solve_using_memoization(index,n,cost):
            # if index >=  n:
            #     return 0
            # r1=solve_using_memoization(index+1,n,cost)
            # r2=solve_using_memoization(index+2,n,cost)
            # return min(r1,r2)+cost[index]
        
#         op1=solve_using_memoization(0,n,cost)
#         op2=solve_using_memoization(1,n,cost)

#         return min(op1,op2)



"""
Memoization

class Solution(object):
    def minCostClimbingStairs(self, cost):
        n=len(cost)
        cache = [-1] * n
        def solve_using_:memoization(index,n,cost):
            if index >=  n
                return 0
            elif cache[index]!= -1:
                return cache[index]
            r1=solve_using_memoization(index+1,n,cost)
            r2=solve_using_memoization(index+2,n,cost)
            cache[index]=min(r1,r2)+cost[index]
            return cache[index]
        
        op1=solve_using_memoization(0,n,cost)
        op2=solve_using_memoization(1,n,cost)

        return min(op1,op2)
"""

"""

TABULATION

"""
class Solution(object):
    def minCostClimbingStairs(self, cost):
        n=len(cost)
        def min_usingTabulation(cost):
            cache=[-1] *(n+2) # Because we can either move one or 2 steps from end
            cache[n] =0
            cache[n+1] =0
            for i in range(n-1,-1,-1):
                r1=cache[i+1]
                r2=cache[i+2]
                cache[i] = min(r1,r2)+cost[i]

            return min(cache[0],cache[1])

        return min_usingTabulation(cost)
    
    