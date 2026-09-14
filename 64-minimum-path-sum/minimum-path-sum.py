class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        dp=[[-1]*n for _ in range(m)]
        dp[0][0]=grid[0][0]
        maxi=(1 << 31) - 1
        for i in range(m):
            for j in range(n):
                if i==0 and j==0:
                    continue
                if i-1>=0:
                    left=dp[i-1][j]+grid[i][j]
                else:
                    left=maxi
                if j-1>=0:
                    up=dp[i][j-1]+grid[i][j]
                else:
                    up=maxi
                dp[i][j]=min(left,up)
        print(dp)
        return dp[m-1][n-1]
        