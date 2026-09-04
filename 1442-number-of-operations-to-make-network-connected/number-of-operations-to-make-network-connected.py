class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)+1<n:
            return -1
        par=[0]*n
        res=n
        for i in range(n):
            par[i]=i
        size=[1]*n
        def ult_par(u):
            if par[u]==u:
                return u
            par[u]=ult_par(par[u])
            return par[u]
        for u,v in connections:
            pu=ult_par(u)
            pv=ult_par(v)
            if pu==pv:
                continue
            if size[pv]>size[pu]:
                par[pu]=pv
                size[pv]+=size[pu]
            else:
                par[pv]=pu
                size[pu]+=size[pv]
            res-=1
        # print(par)
        # s=set()
        # for i in range(len(par)):
        #     s.add(ult_par(i))
        return res-1




        