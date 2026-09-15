class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s=sum(nums)
        if s%2==1:
            return False
        target=s//2
        dp=[[-1]*(target+1) for _ in range(len(nums)) ]
        def f(i,sum):
            if sum==target:
                return True
            if i==0:
                return sum + nums[0] == target
            if dp[i][sum]!=-1:
                return dp[i][sum]
            nottake=f(i-1,sum)
            take=False
            if sum+nums[i]<=target:
                take=f(i-1,sum+nums[i])
            dp[i][sum]=take or nottake
            return take or nottake
        return f(len(nums)-1,0)
        