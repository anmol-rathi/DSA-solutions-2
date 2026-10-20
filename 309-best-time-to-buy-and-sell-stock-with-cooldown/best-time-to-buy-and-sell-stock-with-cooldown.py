class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        dp=[[-1]*2 for _ in range(n)]
        def f(i,buy):
            if i>=n:
                return 0
            if dp[i][buy]!=-1:
                return dp[i][buy]
            if buy:
                profit=max(-prices[i]+f(i+1,0),0+f(i+1,1))
            else:
                profit=max(prices[i]+f(i+2,1),0+f(i+1,0))
            dp[i][buy]=profit
            return profit
        return f(0,1)