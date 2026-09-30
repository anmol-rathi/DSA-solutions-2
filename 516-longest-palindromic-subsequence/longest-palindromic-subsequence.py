class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        dp=[[-1]*n for _ in range(n)]
        def f(i,j):
            if i>j:
                return 0
            if i==j:
                return 1
            if dp[i][j]!=-1:
                return dp[i][j]
            if s[i]==s[j]:
                dp[i][j]=2+f(i+1,j-1)
                return dp[i][j]
            dp[i][j]=max(f(i+1,j),f(i,j-1))
            return dp[i][j]
        return f(0,n-1)
        