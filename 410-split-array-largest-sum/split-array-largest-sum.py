class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left=max(nums)
        right=sum(nums)
        
        def issafe(mid):
            element=1
            total=0
            for i in nums:
                if total+i>mid:
                    total=i
                    element+=1
                else:
                    total+=i
                if element>k:
                    return False
            return True
        while left<=right:
            mid=(left+right)//2
            if issafe(mid):
                right=mid-1
            else:
                left=mid+1
        
        return left

        