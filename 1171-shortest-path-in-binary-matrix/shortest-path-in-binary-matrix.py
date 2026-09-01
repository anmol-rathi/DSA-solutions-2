class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        path=[[-1,-1],[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1]]
        queue=[[0,0,1]]
        visited=[[float("inf")] * n for _ in range(n)]
        visited[0][0]=1
        # print(visited)
        while queue:
            row,col,count=queue.pop(0)
            if row==n-1 and col==n-1:
                return count
            for i,j in path:
                nrow=row+i
                ncol=col+j
                if 0<=nrow<n and 0<=ncol<n:
                    # print(nrow,ncol)
                    if (grid[nrow][ncol]==0) and (visited[nrow][ncol]>count+1):
                        queue.append([nrow,ncol,count+1])
                        visited[nrow][ncol]=count+1
        return -1

        
        