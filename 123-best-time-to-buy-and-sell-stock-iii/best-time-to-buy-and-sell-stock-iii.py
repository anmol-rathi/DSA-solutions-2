class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        dp=[[[-1]*3 for _ in range(2)] for _ in range(n)]
        def f(i,buy,cap):
            if cap==0:
                return 0
            if i==n:
                return 0
            if dp[i][buy][cap]!=-1:
                return dp[i][buy][cap]
            if buy:
                profit=max(-prices[i]+f(i+1,0,cap),f(i+1,1,cap))
            else:
                profit=max(prices[i]+f(i+1,1,cap-1),f(i+1,0,cap))
            dp[i][buy][cap]=profit
            return profit
        return f(0,1,2)