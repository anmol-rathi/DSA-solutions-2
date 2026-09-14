class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[-1]*n for _ in range(m)]
        def f(i,j):
            if i==0 and j==0:
                return 1
            if i<0 or j<0:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            up=f(i-1,j)
            left=f(i,j-1)
            dp[i][j]=up+left
            return up+left
        return f(m-1,n-1)
        


        # total=m+n-2
        # maxi=max(m,n) -1
        # mini=min(m,n) -1
        # res=1
        # while total!=maxi:
        #     res*=total
        #     total-=1
            
        # res=res/factorial(mini)
        # return int(res)

        