class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        c1=0
        c2=0
        def par(s,c1,c2):
            if len(s)==2*n:
                res.append(s)
                return
            if c1<n:
                
                par(s+'(',c1+1,c2)
            # s.pop()
            if c2<c1:
                par(s+')',c1,c2+1)
        res=[]
        par('',c1,c2)
        return res
        

