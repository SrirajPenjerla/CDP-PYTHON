# memoization
class Solution(object):
    def rob(self, nums):
        n=len(nums)
        cache=[-1] * (n+2)
        def max_rob(index,nums):
            if index >= len(nums):
                return 0
            elif cache[index] !=-1:
                return cache[index]
            robcurr=nums[index]+max_rob(index+2,nums)
            skipcurr=max_rob(index+1,nums)
            cache[index]=max(robcurr,skipcurr)
            return cache[index]
        return max_rob(0,nums)
    

# tabulation
class Solution(object):
    def rob(self, nums):
        n=len(nums)
        def max_rob(nums):
            cache=[-1]*(n+2)
            cache[n]= 0
            cache[n+1]=0
            for index in range(n-1,-1,-1):
                robCurrent=nums[index]+cache[index+2]
                skipCurrent=cache[index+1]
                cache[index] = max(robCurrent,skipCurrent)
            return cache[0]
        return max_rob(nums)