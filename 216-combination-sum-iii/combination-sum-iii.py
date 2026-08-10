class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        def com(i,k,arr,s):    
            if n>45:
                return None
            if k==0:
                if s==n:
                    res.append(arr.copy())
                return
                
            if i>=9 or s>n:
                return
            arr.append(i+1)
            com(i+1,k-1,arr,s+i+1)
            arr.pop()
            com(i+1,k,arr,s)
        arr=[]
        com(0,k,arr,0)
        return res
        
        
        