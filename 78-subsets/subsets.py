class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def sub(i,arr):
            if i>=n:
                res.append(arr.copy())
                return
            arr.append(nums[i])
            sub(i+1,arr)
            arr.remove(nums[i])
            sub(i+1,arr)
        n=len(nums)
        res=[]
        sub(0,[])
        return res
        