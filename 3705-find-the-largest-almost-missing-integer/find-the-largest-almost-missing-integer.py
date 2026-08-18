class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n=len(nums)
        h=Counter(nums)
        print(h)
        if k==1:
            m=-1
            for i in h:
                if h[i]==1 and i>m:
                    m=i
            return m
        if k==n:
            return max(nums)
        else:
            if h[nums[0]]>1 and h[nums[n-1]]>1:
                return -1
            elif h[nums[0]]>1:
                return nums[n-1]
            elif h[nums[n-1]]>1:
                return nums[0]
            else:
                return max(nums[0],nums[n-1])
        