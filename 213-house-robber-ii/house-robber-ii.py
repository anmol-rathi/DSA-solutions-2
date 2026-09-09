class Solution:
    def rob(self, nums: List[int]) -> int:
        def get_max(nums):
            prev2=0
            prev=nums[0]
            for val in range(1,len(nums)):
                take=nums[val]
                if val-2>=0:
                    take+=prev2
                nottake=prev
                curr=max(take,nottake)
                prev2=prev
                prev=curr
            return prev
        if len(nums)==1:
            return nums[0]
        return max(get_max(nums[1:]),get_max(nums[:-1]))

                
        