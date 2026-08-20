class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m=len(grid)
        n=len(grid[0])
        visited=set()
        res=0
        for i in range(m):
            for j in range(n):
                queue=[]
                if grid[i][j] == "1" and (i,j) not in visited:
                    visited.add((i,j))
                    queue.append([i,j])
                    res+=1
                    while queue:
                        row,col=queue.pop(0)
                        if row+1<m and grid[row+1][col]=="1" and (row+1,col) not in visited:
                            visited.add((row+1,col))
                            queue.append([row+1,col])
                        if col+1<n and grid[row][col+1]=="1" and (row,col+1) not in visited:
                            visited.add((row,col+1))
                            queue.append([row,col+1])
                        if row-1>=0 and grid[row-1][col]=="1" and (row-1,col) not in visited:
                            visited.add((row-1,col))
                            queue.append([row-1,col])
                        if col-1>=0 and grid[row][col-1]=="1" and (row,col-1) not in visited:
                            visited.add((row,col-1))
                            queue.append([row,col-1])

        return res
                
        