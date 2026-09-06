class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        subsets=1<<n
        print(subsets)
        res=[]
        for i in range(subsets):
            arr=[]
            for j in range(n):
                if (i& (1<<j)):
                    arr.append(nums[j])
            res.append(arr)
        return res
        # def sub(i,arr):
        #     if i>=n:
        #         res.append(arr.copy())
        #         return
        #     arr.append(nums[i])
        #     sub(i+1,arr)
        #     arr.remove(nums[i])
        #     sub(i+1,arr)
        # n=len(nums)
        # res=[]
        # sub(0,[])
        # return res
        