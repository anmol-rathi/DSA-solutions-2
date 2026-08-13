class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        
        n=len(nums)
        if n==1:
            return nums[0]
        l=0
        r=n-1
        while l<=r:
            mid=(l+r)//2
            if mid+1>=n and nums[mid]!=nums[mid-1]:
                return nums[mid]
            if mid-1<0 and nums[mid]!=nums[mid+1]:
                return nums[mid]
            if nums[mid]!=nums[mid-1] and nums[mid]!=nums[mid+1]:
                return nums[mid]
            elif nums[mid-1]==nums[mid]:
                if (mid-l+1)%2==0:
                    l=mid+1
                else:
                    r=mid-2
            else:
                if (mid-l)%2==0:
                    l=mid+2
                else:
                    r=mid-1

        