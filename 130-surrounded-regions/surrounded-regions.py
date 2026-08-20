class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        visited=set()
        queue=[]
        for i in range(m):
            for j in range(n):
                if board[i][j]=="O" and (i,j) not in visited:
                    print(i,j)
                    arr=[]
                    arr.append((i,j))
                    visited.add((i,j))
                    queue.append((i,j))
                    change=1
                    while queue:
                        row,col=queue.pop(0)
                        if row==0 or row+1==m or col==0 or col+1==n:
                            change=0
                        if row-1>=0 and board[row-1][col]=="O" and (row-1,col) not in visited:
                            visited.add((row-1,col))
                            queue.append((row-1,col))
                            arr.append((row-1,col))
                        if row+1<m and board[row+1][col]=="O" and (row+1,col) not in visited:
                            visited.add((row+1,col))
                            queue.append((row+1,col))
                            arr.append((row+1,col))
                        if col-1>=0 and board[row][col-1]=="O" and (row,col-1) not in visited:
                            visited.add((row,col-1))
                            queue.append((row,col-1))
                            arr.append((row,col-1))
                        if col+1<n and board[row][col+1]=="O" and (row,col+1) not in visited:
                            visited.add((row,col+1))
                            queue.append((row,col+1))
                            arr.append((row,col+1))
                    if change==1:
                        for row,col in arr:
                            board[row][col]="X"

        