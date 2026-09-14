class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n=len(matrix)
        dp=[[0]*n for _ in range(n)]
        for i in range(n):
            dp[0][i]=matrix[0][i]
        for i in range(1,n):
            for j in range(n):
                right=dp[i-1][j-1] if j-1>=0 else float('inf')
                middle=dp[i-1][j]
                left=dp[i-1][j+1] if j+1<n else float('inf')
                dp[i][j]=min(right,middle,left) +matrix[i][j]
        # print(dp)
        return min(dp[n-1])

        