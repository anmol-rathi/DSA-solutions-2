class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n=len(accounts)
        par=[-1]*n
        for i in range(n):
            par[i]=i
        size=[1]*n
        # print(par)
        h={}
        def ult_par(u):
            if par[u]==u:
                return u
            par[u]=ult_par(par[u])
            return par[u]
        for i in range(n):
            m=len(accounts[i])
            for j in range(m):
                if j==0:
                    continue
                if accounts[i][j] not in h:
                    h[accounts[i][j]]=i
                else:
                    pu=ult_par(i)
                    pv=ult_par(h[accounts[i][j]])
                    if size[pu]>size[pv]:
                        par[pv]=pu
                        size[pu]+=size[pv]
                    else:
                        par[pu]=pv
                        size[pv]+=size[pu]
        # print(par)
        res={}
        for i in h:
            up=ult_par(h[i])  
            if up in res:
                res[up].append(''.join(i))
            else:
                res[up]=[i]
        # print(res)
        return [[accounts[i][0]]+sorted(emails) for i,emails in res.items()]
                





                