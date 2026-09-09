class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2:
            return max(nums)
        m=[-1]*n
        m[0]=nums[0]
        m[1]=nums[1]
        prev=0
        prev2=0
        for i in range(2,n):
            prev2=m[i-2]
            if i-3 >=0:
                prev=m[i-3]
            m[i]=(nums[i]+max(prev,prev2))
        return max(m[-1],m[-2])

        