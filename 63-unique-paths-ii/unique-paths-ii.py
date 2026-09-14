class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[0][0]==1 or obstacleGrid[m-1][n-1]==1:
            return 0
        dp=[[-1]*n for _ in range(m)]
        def f(i,j):
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            if obstacleGrid[i][j]==1:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            up=f(i-1,j)
            left=f(i,j-1)
            dp[i][j]=up+left
            return up+left
        return f(m-1,n-1)
        