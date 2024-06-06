"""
The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

 

Example 1:


Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
Example 2:

Input: n = 1
Output: [["Q"]]
"""
def isPossible( row, col, board, n):
    # Check-1 --> same row, left cols
    prevCol = col - 1
    while prevCol >= 0:
        if board[row][prevCol] == 1:
            return False 
        prevCol -= 1

    # Check-2 --> left upper diagnol 
    prevRow, prevCol = row - 1, col - 1 
    while prevRow >= 0 and prevCol >= 0:
        if board[prevRow][prevCol] == 1:
            return False 
        prevRow -= 1 
        prevCol -= 1

    # Check-3 --> left lower diagnol
    nextRow, prevCol = row + 1, col - 1 
    while nextRow < n and prevCol >= 0:
        if board[nextRow][prevCol] == 1:
            return False 
        nextRow += 1 
        prevCol -= 1

    return True

def Nqueens(col,n,board,result):
    if col == n:
        currResult = []
        for i in range(n):
            word = ""
            for j in range(n):
                if board[i][j] == 1:
                    word += "Q"
                else:
                    word += "."
            currResult.append(word)
        result.append(currResult)
        return
    
    for row in range(n):
        if isPossible(row,col,board,n):
            board[row][col] = 1
            Nqueens(col+1,n,board,result)
            board[row][col] =0
board=[]
for i in range(4):
            row = []
            for j in range(4):
                row.append(0)
            board.append(row)
result=[]
Nqueens(0,4,board,result)
print(result,end="\n")