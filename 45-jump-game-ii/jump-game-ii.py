class Solution:
    def jump(self, nums: List[int]) -> int:
        j=0
        l=0
        r=0
        n=len(nums)
        while r<n-1:
            far=0
            for i in range(l,r+1):
                far=max(far,i+nums[i])
            l=r+1
            r=far
            j+=1
        return j

            
        