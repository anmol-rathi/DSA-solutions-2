class Solution:
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        dp={}
        def f(i,tar):
            if i==0:
                if nums[0]==0 and tar==0:
                    return 2
                elif nums[0]==abs(tar):
                    return 1
                else:
                    return 0
            if (i,tar) in dp:
                return dp[(i,tar)]
            add=f(i-1,tar-nums[i])
            subtract=f(i-1,tar+nums[i])
            dp[(i,tar)]= add+subtract
            return add+subtract
        n=len(nums)
        return f(n-1,target)