class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=set()
        queue=[]
        for i in range(n):
            if grid[0][i]==1 and (0,i) not in visited:
                visited.add((0,i))
                queue.append((0,i))
                while queue:
                    row,col=queue.pop(0)
                    if row-1>=0 and grid[row-1][col]==1 and (row-1,col) not in visited:
                            visited.add((row-1,col))
                            queue.append((row-1,col))      
                    if row+1<m and grid[row+1][col]==1 and (row+1,col) not in visited:
                        visited.add((row+1,col))
                        queue.append((row+1,col))  
                    if col-1>=0 and grid[row][col-1]==1 and (row,col-1) not in visited:
                        visited.add((row,col-1))
                        queue.append((row,col-1)) 
                    if col+1<n and grid[row][col+1]==1 and (row,col+1) not in visited:
                        visited.add((row,col+1))
                        queue.append((row,col+1))
        for i in range(n):
            if grid[m-1][i]==1 and (m-1,i) not in visited:
                visited.add((m-1,i))
                queue.append((m-1,i))
                while queue:
                    row,col=queue.pop(0)
                    if row-1>=0 and grid[row-1][col]==1 and (row-1,col) not in visited:
                            visited.add((row-1,col))
                            queue.append((row-1,col))      
                    if row+1<m and grid[row+1][col]==1 and (row+1,col) not in visited:
                        visited.add((row+1,col))
                        queue.append((row+1,col))  
                    if col-1>=0 and grid[row][col-1]==1 and (row,col-1) not in visited:
                        visited.add((row,col-1))
                        queue.append((row,col-1)) 
                    if col+1<n and grid[row][col+1]==1 and (row,col+1) not in visited:
                        visited.add((row,col+1))
                        queue.append((row,col+1))
        for i in range(1,m-1):
            if grid[i][0]==1 and (i,0) not in visited:
                visited.add((i,0))
                queue.append((i,0))
                while queue:
                    row,col=queue.pop(0)
                    if row-1>=0 and grid[row-1][col]==1 and (row-1,col) not in visited:
                            visited.add((row-1,col))
                            queue.append((row-1,col))      
                    if row+1<m and grid[row+1][col]==1 and (row+1,col) not in visited:
                        visited.add((row+1,col))
                        queue.append((row+1,col))  
                    if col-1>=0 and grid[row][col-1]==1 and (row,col-1) not in visited:
                        visited.add((row,col-1))
                        queue.append((row,col-1)) 
                    if col+1<n and grid[row][col+1]==1 and (row,col+1) not in visited:
                        visited.add((row,col+1))
                        queue.append((row,col+1))
        for i in range(1,m-1):
            if grid[i][n-1]==1 and (i,n-1) not in visited:
                visited.add((i,n-1))
                queue.append((i,n-1))
                while queue:
                    row,col=queue.pop(0)
                    if row-1>=0 and grid[row-1][col]==1 and (row-1,col) not in visited:
                            visited.add((row-1,col))
                            queue.append((row-1,col))      
                    if row+1<m and grid[row+1][col]==1 and (row+1,col) not in visited:
                        visited.add((row+1,col))
                        queue.append((row+1,col))  
                    if col-1>=0 and grid[row][col-1]==1 and (row,col-1) not in visited:
                        visited.add((row,col-1))
                        queue.append((row,col-1)) 
                    if col+1<n and grid[row][col+1]==1 and (row,col+1) not in visited:
                        visited.add((row,col+1))
                        queue.append((row,col+1))
        count=0
        for i in range(1,m):
            for j in range(1,n):
                if grid[i][j]==1 and (i,j) not in visited:
                    count+=1
        return count
        
                        
                    
