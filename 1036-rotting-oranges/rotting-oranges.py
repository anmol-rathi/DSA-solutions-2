class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=set()
        queue=[]
        count=0
        check=[]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    check.append((i,j))
                if grid[i][j]==2 and (i,j) not in visited:
                    visited.add((i,j))
                    queue.append((i,j))
        while queue:
            p=len(visited)
            for _ in range(len(queue)):
                row,col=queue.pop(0)
                if row-1>=0 and grid[row-1][col]==1:
                    grid[row-1][col]=2
                    visited.add((row-1,col))
                    queue.append((row-1,col))
                if row+1<m and grid[row+1][col]==1:
                    grid[row+1][col]=2
                    visited.add((row+1,col))
                    queue.append((row+1,col))
                if col-1>=0 and grid[row][col-1]==1:
                    grid[row][col-1]=2
                    visited.add((row,col-1))
                    queue.append((row,col-1))
                if col+1<n and grid[row][col+1]==1:
                    grid[row][col+1]=2
                    visited.add((row,col+1))
                    queue.append((row,col+1))
            if len(visited)>p:
                count+=1
        for i,j in check:
            if (i,j) not in visited:
                return -1
        return count


