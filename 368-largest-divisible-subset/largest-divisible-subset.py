class Solution:
    def largestDivisibleSubset(self, nums: list[int]) -> list[int]:
        nums.sort()
        n=len(nums)
        dp=[1]*n
        prevele=[-1]*n
        lastindex=0

        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j]==0:
                    if dp[i]< 1+dp[j]:
                        dp[i]=1+dp[j]
                        prevele[i]=j
            if dp[i]>dp[lastindex]:
                lastindex=i
        res=[]
        while lastindex!=-1:
            res.append(nums[lastindex])
            lastindex=prevele[lastindex]
        return res[::-1]