class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n=len(coins)
        def f(i,tar):
            # print(i,tar)
            if i==0:
                if tar%coins[i]==0:
                    return 1
                else:
                    return 0
            if dp[i][tar]!= -1:
                return dp[i][tar]
            nottake=f(i-1,tar)
            take=0
            if coins[i]<=tar:
                take=f(i,tar-coins[i])
            dp[i][tar]=take+nottake
            return take+nottake
        dp=[[-1]*(amount+1) for _ in range(n)]
        # print(dp)
        return f(n-1,amount)        