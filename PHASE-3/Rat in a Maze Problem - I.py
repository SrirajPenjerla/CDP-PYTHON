'''
link ::: https://www.geeksforgeeks.org/problems/rat-in-a-maze-problem/1


Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1).
 Find all possible paths that the rat can take to reach from source to destination. The directions in which the rat 
 can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and
 rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
Note: In a path, no cell can be visited more than one time. If the source cell is 0, the rat cannot move to any other cell.

Example 1:

Input:
N = 4
m[][] = {{1, 0, 0, 0},
         {1, 1, 0, 1}, 
         {1, 1, 0, 0},
         {0, 1, 1, 1}}
Output:
DDRDRR DRDDRR
Explanation:
The rat can reach the destination at 
(3, 3) from (0, 0) by two paths - DRDDRR 
and DDRDRR, when printed in sorted order 
we get DDRDRR DRDDRR.
Example 2:
Input:
N = 2
m[][] = {{1, 0},
         {1, 0}}
Output:
-1
Explanation:
No path exists and destination cell is 
blocked.

D -- down
R -- right
L -- left
U -- up
'''
def find_route(arr,x,y,path,vis,n):
    if x<0 or x == n or y<0 or y==n  :
        return 
    if arr[x][y] == 0 or vis[x][y] == True:
        return
    if x == n-1 and y == n-1:
        print("".join(path))
        return
    vis[x][y] = True
    # print(path)
    path.append("U")
    find_route(arr,x-1,y,path,vis,n)
    path.pop()

    path.append("D")
    find_route(arr,x+1,y,path,vis,n)
    path.pop()

    path.append("L")
    find_route(arr,x,y-1,path,vis,n)
    path.pop()

    path.append("R")
    find_route(arr,x,y+1,path,vis,n)
    path.pop()

    vis[x][y] = False



# arr = [[1, 1, 0, 0], [1, 1, 1, 1], [1, 1, 1, 0], [1, 1, 1, 1]]
arr=[[1, 0, 0, 0],
         [1, 1, 0, 1], 
         [1, 1, 0, 0],
         [0, 1, 1, 1]]
vis=[]
n=len(arr)
for i in range(n):
	eachRow = []
	for j in range(n):
		eachRow.append(False)
	vis.append(eachRow)
find_route(arr,0,0,[],vis,len(arr))
