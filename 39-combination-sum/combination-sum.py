class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        arr=[]
        n=len(candidates)
        def com(i,arr):
            if i>=n:
                return
            if sum(arr)==target:
                # print(arr)
                res.append(arr.copy())
                # print(res)
                return
            if sum(arr)>target:
                return
            arr.append(candidates[i])
            com(i,arr)
            arr.remove(candidates[i])
            com(i+1,arr)
        
        com(0,arr)
        return res
        
        
        