class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            nums[i]=nums[i]*nums[i]
        nums.sort()
        # print(nums)
        res=0
        for i in range(n):
            if i<n//2:
                res-=nums[i]
            else:
                res+=nums[i]
        return res
