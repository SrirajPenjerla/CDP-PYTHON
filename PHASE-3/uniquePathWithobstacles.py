class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        cache=[]
        for i in range(m):
            s=[-1] * n
            cache.append(s)
        def solveIt(x,y):
            if x>=m or y>=n:
                return 0
            if obstacleGrid[x][y] == 1:
                return 0
            if x == m-1 and y  == n-1:
                return 1
            elif cache[x][y] !=-1:
                return cache[x][y]
            r1=solveIt(x+1,y)
            r2=solveIt(x,y+1)

            cache[x][y]=r1+r2

            return cache[x][y]
        return solveIt(0,0)
        