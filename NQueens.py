def isSafe(col,row,board,n):
    dupcol =col
    duprow = row
    while(col>=0 and row>=0):
        if board[row][col]=="Q":
            return False
        row-=1
        col-=1
    col = dupcol
    row = duprow
    while col>=0:
        if board[row][col]=="Q":
            return False
        col-=1
    col = dupcol
    row = duprow
    while col>=0 and row<n:
        
        
        if board[row][col]=="Q":
            return False
        col-=1
        row+=1
    return True


# . . Q .
# Q . . .
# . . . Q
# . Q . .
# . Q . .
# . . . Q
# Q . . .
# . . Q .
    
def NQueen(col,board,ans,n):
    if col==len(board):
        # print(board)
        for i in board:
            print(*i)
        ans.append(board)
        return
    for row in range(0,n):
        if isSafe(col,row,board,n):
            # print(board)
            board[row][col]="Q"
            NQueen(col+1,board,ans,n)
            board[row][col]="."
            
            
    
ans=[]
board =[[".",".",".","."],[".",".",".","."],[".",".",".","."],[".",".",".","."]]

NQueen(0,board,ans,4)
