class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(s), len(t)
        if m < n:
            return 0
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][n] = 1
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j]
        
        return dp[0][0]
        # res=0
        # def same(subs,i):
        #     nonlocal res
        #     if len(subs)==len(t):
        #         if subs==t:
        #             res+=1
        #         return
        #     if i>=len(s):
        #         return
        #     n=len(subs)
        #     if subs == t[:n]:
                
        #         same(subs+s[i],i+1)
                
        #         same(subs,i+1)
        # same('',0)
        # # print(res)
        # return res

        