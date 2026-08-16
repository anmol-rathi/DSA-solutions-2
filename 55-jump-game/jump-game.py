class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i=0
        n=len(nums)
        jump=0
        if n==1:
            return True
        while i<n-1:
            jump=max(jump,nums[i])
            if jump<=0:
                return False
            i+=1
            jump-=1
        return True
        