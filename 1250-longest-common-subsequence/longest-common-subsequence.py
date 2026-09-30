class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n=len(text1)
        m=len(text2)
        dp=[[-1]*m for _ in range(n)]
        def f(i1,i2):
            if (i1<0 or i2<0):
                return 0
            if dp[i1][i2]!=-1:
                return dp[i1][i2]
            if text1[i1]==text2[i2]:
                dp[i1][i2]= 1+f(i1-1,i2-1)
                return dp[i1][i2]
            dp[i1][i2]=max(f(i1-1,i2),f(i1,i2-1))
            return dp[i1][i2]
        return f(n-1,m-1)
        