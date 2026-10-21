class Solution:
    def findNumberOfLIS(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        lengths = [1] * n
        counts = [1] * n
        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lengths[j] + 1 > lengths[i]:
                        lengths[i] = lengths[j] + 1
                        counts[i] = counts[j] #inherit
                    elif lengths[j] + 1 == lengths[i]:
                        counts[i] += counts[j] #add
        maxi=max(lengths)
        res=0
        for i in range(n):
            if lengths[i]==maxi:
                res+= counts[i]
        return res