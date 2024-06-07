def findLargestDiagonal(x,y,mat,ans,f):
    if x >len(mat) or x<0 or y<0 or y>len(mat):
        return 
    if y ==len(mat):
        f.append(ans)
        return 
    if mat[x][y] == 1:
        ans.append((x,y))
        # trying to expand it further in upwardcc
        findLargestDiagonal(x-1,y-1,mat,ans,f)
        #Tryint to expand it in downward direction
        findLargestDiagonal(x+1,y+1,mat,ans,f)
        # findLargestDiagonal(x-1,y+1,mat,ans,f)
        # findLargestDiagonal(x+1,y-1,mat,ans,f)
        ans.pop()
    else:
        return


mat=[[1,1,1,1,0,1],
     [0,1,1,0,1,0],
     [1,0,1,1,0,1],
     [0,1,1,0,1,0],
     [1,1,1,0,0,1]]

f=[]
ans=[]
findLargestDiagonal(0,0,mat,ans,f)
print(f)
    
 