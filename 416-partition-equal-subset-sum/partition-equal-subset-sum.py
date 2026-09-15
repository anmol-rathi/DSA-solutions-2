class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if s%2==1:
            return False
        dp=[[-1]*((s//2)+1) for _ in range(len(nums)) ]
        def f(i,sum):
            if sum==s/2:
                return True
            if i==0:
                return False
            if dp[i][sum]!=-1:
                return dp[i][sum]
            nottake=f(i-1,sum)
            take=False
            if sum+nums[i]<=s/2:
                take=f(i-1,sum+nums[i])
            dp[i][sum]=take or nottake
            return take or nottake
        return f(len(nums)-1,0)
        