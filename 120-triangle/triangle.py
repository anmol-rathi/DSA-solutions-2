class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n=len(triangle)
        dp=[]
        for i in range(n):
            temp=[]
            for j in range(i+1):
                temp.append(-1)
            dp.append(temp)
        dp[0][0]=triangle[0][0]
        for i in range(1,n):
            for j in range(i+1):
                prev=dp[i-1][j-1] if j-1>=0 else float('inf')
                curr=dp[i-1][j] if j<=i-1 else float('inf')
                dp[i][j]= min(prev,curr) + triangle[i][j]
        return min(dp[n-1])
                
        