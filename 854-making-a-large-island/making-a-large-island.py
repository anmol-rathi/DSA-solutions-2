class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n=len(grid)
        par=[i for i in range(n*n)]
        # print(par)
        size=[1]*(n*n)
        # print(size)
        arr=[]
        direction=[[-1,0],[0,1],[1,0],[0,-1]]
        def ult_par(u):
            if par[u]==u:
                return u
            par[u]=ult_par(par[u])
            return par[u]
        for i in range(n):
            for j in range(n):
                if grid[i][j]==0:
                    arr.append([i,j])
                else:
                    for x,y in direction:
                        newr=i+x
                        newc=j+y
                        if 0<=newr<n and 0<=newc<n and grid[newr][newc]==1:
                            pu=ult_par((i*n)+j)
                            pv=ult_par((newr*n)+newc)
                            if pu==pv:
                                continue
                            if size[pu]>size[pv]:
                                par[pv]=pu
                                size[pu]+=size[pv]
                            else:
                                par[pu]=pv
                                size[pv]=size[pv]+size[pu]
        # print(par)
        # print(size)
        # print(arr)
        m=0
        if not arr:
            return n*n
        for i,j in arr:
            index=(i*n)+j
            s=set()
            temp=0
            for x,y in direction:
                newr=i+x
                newc=j+y
                if 0<=newr<n and 0<=newc<n and grid[newr][newc]==1:
                    pu=(newr*n)+newc
                    pu=ult_par(pu)
                    # print(pu)
                    s.add(pu)
            # print(s)
            for num in s:
                temp+=size[num]
            m=max(m,temp+1)
        # print(m)
        return m

                


                            
                    




        