class Solution:
    def lastStoneWeightII(self, stones: list[int]) -> int:
        n=len(stones)
        s=sum(stones)
        target=s//2
        dp=[[False]*(target+1) for _ in range(n)]
        for i in range(n):
            dp[i][0]=True
        if stones[0]<=target:
            dp[0][stones[0]]=True
        for i in range(1,n):
            for j in range(1,target+1):
                nottake=dp[i-1][j]
                take=False
                if j>=stones[i]:
                    take=dp[i-1][j-stones[i]]
                dp[i][j]=take or nottake
        # print(dp)
        mini=float('inf')
        for i in range((target)+1):
            if dp[n-1][i]:
                mini=min(mini,abs(s-(2*i)))
        # print(mini)
        return mini


        