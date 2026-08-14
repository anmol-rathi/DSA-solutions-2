class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def issafe(mid):
            temp=threshold
            for i in nums:
                temp-=i//mid
                if (i%mid)!=0:
                    temp-=1
                if temp<0:
                    return False
            return True
        left=1
        right=max(nums)
        while left<=right:
            mid=(left+right)//2
            if issafe(mid):
                right=mid-1
            else:
                left=mid+1
        return left
        