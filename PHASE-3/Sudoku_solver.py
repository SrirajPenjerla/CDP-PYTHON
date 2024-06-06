'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
The '.' character indicates empty cells.

 

Example 1:


Input: board = [["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]]



Output:    [["5","3","4","6","7","8","9","1","2"],
            ["6","7","2","1","9","5","3","4","8"],
            ["1","9","8","3","4","2","5","6","7"],
            ["8","5","9","7","6","1","4","2","3"],
            ["4","2","6","8","5","3","7","9","1"],
            ["7","1","3","9","2","4","8","5","6"],
            ["9","6","1","5","3","7","2","8","4"],
            ["2","8","7","4","1","9","6","3","5"],
            ["3","4","5","2","8","6","1","7","9"]]


Explanation: The input board is shown above and the only valid solution is shown below:


 

Constraints:

board.length == 9
board[i].length == 9
board[i][j] is a digit or '.'.
It is guaranteed that the input board has only one solution.'''




        
    
    
# mat=       [["5","3","4","6","7","8","9","1","2"],
#             ["6","7","2","1","9","5","3","4","8"],
#             ["1","9","8","3","4","2","5","6","7"],
#             ["8","5","9","7","6","1","4","2","3"],
#             ["4","2","6","8","5","3","7","9","1"],
#             ["7","1","3","9","2","4","8","5","6"],
#             ["9","6","1","5","3","7","2","8","4"],
#             ["2","8","7","4","1","9","6","3","5"],
#             ["3","4","5","2","8","6","1","7","9"]]

# # mat=[[1,2,3],
# #      [1,2,3],
# #      [1,2,3]]
        
# print_Mat(9,0,0,mat)


def is_possible(x,y,val,board):
    for col in range(9):
        if board[x][col] == str(val):
            return False
    for row in range(9):
        if board[row][y] == str(val):
            return False
    chex=(x//3)*3
    chey=(y//3)*3
    for i in range(3):
        for j in range(3):
            if board[chex+i][chey+j] == str(val):
                return False
    return True


def Sudoku_solver(x,y,board):
    if x  == 9:
        return True
    # topx,topy=-1,-1
    if y == 8:
        topx=x+1
        topy=0
    else:
        topx=x
        topy=y+1
    if board[x][y] !=".":
        return Sudoku_solver(topx,topy,board)
    
    for i in range(1,10):
        if is_possible(x,y,i,board):
            board[x][y]=str(i)
            res=Sudoku_solver(topx,topy,board)
            if res == True:
                return True
            board[x][y] = '.'

    return False


def print_Mat(n,x,y,mat):
    if x == n:
        return 
    if y == n:
        print()
        return print_Mat(n,x+1,0,mat)
    print(mat[x][y],end="  ")
    print_Mat(n,x,y+1,mat)

board=        [["5","3",".",".","7",".",".",".","."],
                ["6",".",".","1","9","5",".",".","."],
                [".","9","8",".",".",".",".","6","."],
                ["8",".",".",".","6",".",".",".","3"],
                ["4",".",".","8",".","3",".",".","1"],
                ["7",".",".",".","2",".",".",".","6"],
                [".","6",".",".",".",".","2","8","."],
                [".",".",".","4","1","9",".",".","5"],
                [".",".",".",".","8",".",".","7","9"]] 

board=[[".",".",".",".",".",".",".",".","."],
                [".",".",".",".",".",".",".",".","."],
                [".",".",".",".",".",".",".",".","."],
                [".",".",".",".",".",".",".",".","."],
                [".",".",".",".",".",".",".",".","."],
                [".",".",".",".",".",".",".",".","."],
                [".",".",".",".",".",".",".",".","."],
                [".",".",".",".",".",".",".",".","."],
                [".",".",".",".",".",".",".",".","."]]  


print_Mat(9,0,0,board)
Sudoku_solver(0,0,board)
print("after solving ")
print_Mat(9,0,0,board)


# class Solution(object):
#     def is_possible(self,x,y,val,board):
#         for col in range(9):
#             if board[x][col] == str(val):
#                 return False
#         for row in range(9):
#             if board[row][y] == str(val):
#                 return False
#         chex=(x//3)*3
#         chey=(y//3)*3
#         for i in range(3):
#             for j in range(3):
#                 if board[chex+i][chey+j] == str(val):
#                     return False
#         return True


#     def Sudoku_solver(self,x,y,board):
#         if x  == 9:
#             return True
#         topx,topy=-1,-1
#         if y == 8:
#             topx=x+1
#             topy=0
#         else:
#             topx=x
#             topy=y+1
#         if board[x][y] !=".":
#             return self.Sudoku_solver(topx,topy,board)
        
#         for i in range(1,10):
#             if self.is_possible(x,y,i,board):
#                 board[x][y]=str(i)
#                 res=self.Sudoku_solver(topx,topy,board)
#                 if res == True:
#                     return True
#                 board[x][y] = '.'

#         return False
#     def solveSudoku(self, board):
#         """
#         :type board: List[List[str]]
#         :rtype: None Do not return anything, modify board in-place instead.
#         """

#         self.Sudoku_solver(0,0,board)
#         return board
        