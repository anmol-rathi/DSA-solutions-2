class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        n=len(candidates)
        def com(i,arr,tar):
            if tar==target:
                res.append(arr.copy())
                return
            if tar>target:
                return
            if i>=n:
                return
            
            arr.append(candidates[i])
            com(i+1,arr,tar+candidates[i])
            arr.remove(candidates[i])
            while i+1<n and candidates[i]==candidates[i+1]:
                i+=1
            com(i+1,arr,tar)
        res=[]
        candidates.sort()
        com(0,[],0)
        return res

        