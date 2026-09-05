class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        maxr=0
        maxc=0
        for i in stones:
            maxr=max(maxr,i[0])
            maxc=max(maxc,i[1])
        # print(maxr,maxc)
        maxr+=1
        maxc+=1
        par=[i for i in range(maxr+maxc)]
        size=[1]*(maxr+maxc)
        # print(par)
        def ult_par(u):
            if par[u]==u:
                return u
            par[u]=ult_par(par[u])
            return par[u]
        for row,col in stones:
            prow=ult_par(row)
            pcol=ult_par(col+maxr)
            if prow==pcol:
                continue
            if size[prow]>size[pcol]:
                par[pcol]=prow
                size[prow]+=size[pcol]
            else:
                par[prow]=pcol
                size[pcol]+=size[prow]
        print(par,size)
        s=set()
        for row, _ in stones:
            s.add(ult_par(row))
        return len(stones)-len(s)





        
        