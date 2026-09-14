class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[0][0]==1 or obstacleGrid[m-1][n-1]==1:
            return 0
        dp=[[0]*n for _ in range(m)]
        dp[0][0]=1
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                if obstacleGrid[i][j]==1:
                    continue
                if i-1>=0:
                    left=dp[i-1][j]
                else:
                    left=0
                if j-1>=0:
                    up=dp[i][j-1]
                else:
                    up=0
                dp[i][j]=left+up
        return dp[m-1][n-1]
        # def f(i,j):
        #     if i==0 and j==0:
        #         return 1
        #     if i<0 or j<0:
        #         return 0
        #     if obstacleGrid[i][j]==1:
        #         return 0
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
        #     up=f(i-1,j)
        #     left=f(i,j-1)
        #     dp[i][j]=up+left
        #     return up+left
        # return f(m-1,n-1)
        