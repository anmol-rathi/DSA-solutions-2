class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        merged_num=0
        for i in range(len(nums)):
            merged_num^=nums[i]
        rightmost=(merged_num & merged_num-1) ^merged_num
        b1=0
        b2=0
        for i in nums:
            if i&rightmost:
                b1^=i
            else:
                b2^=i
        return [b1,b2]

        