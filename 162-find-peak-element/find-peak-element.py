class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l=0
        n=len(nums)
        if n==1:
            return 0
        r=n-1
        while l<=r:
            mid=(l+r)//2
            if mid-1>=0 and mid+1<n and nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            elif mid-1<0 and nums[mid]>nums[mid+1]:
                return mid
            elif mid+1>=n and nums[mid]>nums[mid-1]:
                return mid
            elif nums[mid+1]>nums[mid]:
                l=mid+1
            else:
                r=mid-1
        