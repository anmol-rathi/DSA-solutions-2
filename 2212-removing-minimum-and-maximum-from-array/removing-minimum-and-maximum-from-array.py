class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        min_num=float("inf")
        max_num=float("-inf")
        minc=-1
        maxc=-1
        for i in range(len(nums)):
            if min_num>nums[i]:
                min_num=nums[i]
                minc=i
            if max_num<nums[i]:
                max_num=nums[i]
                maxc=i
        # print(min_num,max_num,minc,maxc)
        mi=min(minc,maxc)
        ma=max(maxc,minc)
        res=min(ma+1, len(nums)-mi)
        # print(res)
        return min(res, mi+ (len(nums)-ma)+1)

        