class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist=[[distanceThreshold+1]*n for _ in range(n)]
        for i,j,d in edges:
            dist[i][j]=d
            dist[j][i]=d
        for i in range(n):
            dist[i][i]=0
        
        for via in range(n):
            for i in range(n):
                if i==via:
                    continue
                for j in range(n):
                    if j==via or i==j:
                        continue
                    dist[i][j]=min(dist[i][j],dist[i][via]+dist[via][j])
        # print(dist)
        mincount=float('inf')
        res=-1
        for i in range(n):
            count=0
            for j in range(n):
                if dist[i][j]!=0 and dist[i][j]<=distanceThreshold:
                    count+=1
            # print(count)
            if count<=mincount:
                mincount=count
                res=i
        return res



        