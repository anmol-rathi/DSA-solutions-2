class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n=len(graph)
        color=[-1]*n
        for i in range(n):
            if color[i]!=-1:
                continue
            queue=[i]
            color[i]=0
            while queue:
                node=queue.pop(0)
                for j in graph[node]:
                    if color[j]==-1:
                        color[j]=1-color[node]
                        queue.append(j)
                    elif color[j]==color[node]:
                        return False
        return True
                        
            
        