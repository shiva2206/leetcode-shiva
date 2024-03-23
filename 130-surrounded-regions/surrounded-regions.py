class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        d = set()
        def dfs(i,j):
            if 0<=i<len(board) and 0<=j<len(board[i]) and  board[i][j]=='O' and (i,j) not in d:
                d.add((i,j))
                dfs(i,j+1)
                dfs(i,j-1)
                dfs(i+1,j)
                dfs(i-1,j)

        for i in range(0,len(board)):
            if board[i][0]=='O':
                dfs(i,0)
            if board[i][len(board[i])-1]=='O':    
                dfs(i,len(board[i])-1)
        for j in range(len(board[0])):
            if board[0][j]=='O':
                dfs(0,j)
            if board[len(board)-1][j]=='O':    
                dfs(len(board)-1,j)

        for i in range(1,len(board)-1):
            for j in range(1,len(board[i])-1):
                if (i,j) not in d:
                    board[i][j]='X'

        