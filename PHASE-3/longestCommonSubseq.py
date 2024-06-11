class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        cache=[]
        for i in range(len(text1)):
            m=[-1] * len(text2)
            cache.append(m)
        cache[len(text1)-1][len(text2)-1] = 0
        def solveIt(s1,s2,i1,i2):
            if i1>=len(s1) or i2>=len(s2):
                return 0
            if s1[i1] == s2[i2]:
                return 1+solveIt(s1,s2,i1+1,i2+1)
            elif cache[i1][i2]!=-1:
                return cache[i1][i2]
            c1=solveIt(s1,s2,i1+1,i2)
            c2=solveIt(s1,s2,i1,i2+1)
            cache[i1][i2] = max(c1,c2)
            return cache[i1][i2]
        n=len(text1)
        m=len(text2)
        def Tabulation():
            cache=[[0]*(m+1) for i in range(n+1)]
            for i in range(n-1,-1,-1):
                for j in range(m-1,-1,-1):
                    if text1[i] == text2[j]:
                        cache[i][j] = 1+cache[i+1][j+1]
                    else:
                        c1=cache[i+1][j]
                        c2=cache[i][j+1]
                        cache[i][j] =  max(c1,c2)

            return cache[0][0]
        # return solveIt(text1,text2,0,0)
        return Tabulation()

        