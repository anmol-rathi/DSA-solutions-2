class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n=len(nums)
        prefmax=[0]*n
        suffmin=[0]*n
        for i in range(n):
            if i==0:
                prefmax[0]=nums[0]
                suffmin[n-1]=nums[n-1]
                continue
            prefmax[i]=max(prefmax[i-1],nums[i])
            suffmin[n-i-1]=min(suffmin[n-i],nums[n-i-1])
        # print(prefmax,suffmin)
        res=-1
        for i in range(n):
            if k>= prefmax[i]-suffmin[i]:
                res=i
                break
        # print(res)
        return res





        