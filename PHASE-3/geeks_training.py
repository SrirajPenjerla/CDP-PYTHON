#User function Template for python3

class Solution:
    def maximumPoints(self, points, n):
        def takeMax(day,prev):
            if day == n:
                return 0
            
            ans=0
            for i in range(3):
                if i!= prev:
                    currPoints=points[day][i]+takeMax(day+1,i)
                    ans=max(ans,currPoints)
            return ans 
        return takeMax(0,-1)




class Solution:
    def maximumPoints(self, points, n):
        cache=[]
        for i in range(n):
            sub=[-1]*4
            cache.append(sub)
            
        def takeMax(day,prev):
            if day == n:
                return 0
            elif cache[day][prev+1]!=-1:
                return cache[day][prev+1]
            ans=0
            for i in range(3):
                if i!= prev:
                    currPoints=points[day][i]+takeMax(day+1,i)
                    ans=max(ans,currPoints)
            cache[day][prev+1] = ans 
            return ans 
        return takeMax(0,-1)
    


