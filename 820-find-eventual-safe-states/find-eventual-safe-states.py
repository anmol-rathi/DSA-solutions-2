class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n=len(graph)
        state=[0]*n
        def dfs(node):
            state[node]=1
            for i in graph[node]:
                if state[i]==1:
                    return True
                if state[i]==0 and dfs(i):
                    return True
            state[node]=2
            return False
        safe=[]
        for i in range(n):
            if not dfs(i):
                safe.append(i)
        return safe

        