class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n=len(s)
        m=len(t)
        dp=[[-1]*m for _ in range(n)]
        def f(i,j):
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            nottake=f(i-1,j)
            take=0
            if s[i]==t[j]:
                if j==0:
                    # print(i,j)
                    take = 1
                else:
                    take= f(i-1,j-1)
            dp[i][j]=take+nottake
            return dp[i][j]
        return f(len(s)-1,len(t)-1)        