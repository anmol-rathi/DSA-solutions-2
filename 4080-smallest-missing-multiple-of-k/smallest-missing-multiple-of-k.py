class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        s=set(nums)
        i=1
        while True:
            if k*i not in s:
                return k*i
            i+=1
        