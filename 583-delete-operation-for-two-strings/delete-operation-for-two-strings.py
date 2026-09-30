class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n=len(word1)
        m=len(word2)
        dp=[[-1]*m for _ in range(n)]
        def f(i1,i2):
            if (i1<0 or i2<0):
                return 0
            if dp[i1][i2]!=-1:
                return dp[i1][i2]
            if word1[i1]==word2[i2]:
                dp[i1][i2]= 1+f(i1-1,i2-1)
                return dp[i1][i2]
            dp[i1][i2]=max(f(i1-1,i2),f(i1,i2-1))
            return dp[i1][i2]
        return m+n - (2*(f(n-1,m-1)))