class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) < 2 or len(board[0]) < 2:
            return
 
        def dfs(board,i,j):
            
            if (i>=0 and j>=0 and i<len(board) and j<len(board[0]) and board[i][j] == "O"):

                        
              
                board[i][j]='*'
       
                
            
                dfs(board,i-1,j)
            
            
                dfs(board,i+1,j)
                
            
            
                dfs(board,i,j-1)
                
            
                dfs(board,i,j+1)    
            else:
                
                return
                

        row=len(board)
        col=len(board[0])
        
                
        for i in range(len(board)):
            
            if board[i][0] == 'O':
                dfs(board,i,0)
            
            if board[i][col-1] == 'O':
                dfs(board,i,col-1)
        
        for j in range(len(board[0])):
            
            if board[0][j] == 'O':
                dfs(board,0,j)            
            
            if board[row-1][j] == 'O':
                
                dfs(board,row-1,j)
                
                
   
        for i in range(row):
            for j in range(col):
                if board[i][j]=="O":
                    board[i][j]='X'
                    
                elif board[i][j]=='*':
                    board[i][j]='O'
