class Solution(object):
    def uniquePaths(self, m, n):
        if m == 1 and n==1:
            return 1
        cache=[]
        for i in range(m):
            s=[-1]*(n)
            cache.append(s)
        
        def findUnique(x,y):
            if x == m-1 and y == n-1:
                return 1  
            if x>m-1 or y>n-1:
                return 0   
            elif cache[x][y]!= -1:
                return cache[x][y]
            
            p1=findUnique(x+1,y)
            p2=findUnique(x,y+1)
            cache[x][y]=(p1+p2)
            return cache[x][y] 

        ans=0
        return findUnique(0,0)
            
        