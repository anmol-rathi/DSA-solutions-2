class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=Counter(nums)
        m=0
        res=-1
        for i in count:
            if m<count[i]:
                m=count[i]
                res=i
        return res
        