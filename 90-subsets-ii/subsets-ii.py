class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        res=[]
        arr=[]
        def sub(i,arr):
            if i>=n:
                res.append(arr.copy())
                return
            arr.append(nums[i])
            sub(i+1,arr)
            arr.remove(nums[i])
            while i+1<n and nums[i]==nums[i+1]:
                i+=1
            sub(i+1,arr)
        nums.sort()
        sub(0,arr)
        return res
        