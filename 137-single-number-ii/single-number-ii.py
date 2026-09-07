class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        n=len(nums)
        res=0
        for bits in range(32):
            count=0
            for i in nums:
                if i<0:
                    i=i& (2**32 -1)
                if i&(1<<bits):
                    count+=1
            if count%3!=0:
                res=res|(1<<bits)
        if res>=2**31:
            res-=2**32
        return res

                

        # nums.sort()
        # for i in range(1,len(nums),3):
        #     if nums[i]!=nums[i-1]:
        #         return nums[i-1]
        # return nums[len(nums)-1] 
        # # it is o(nlogn+n/3) better than (32n solution)
     
        