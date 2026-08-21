class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited=set()
        h=defaultdict(list)
        for i,j in prerequisites:
            # if i not in h:
            #     h[i]=[j]
            # else:
            h[i].append(j)
        def dfs(node):
            if node in visited:
                return False
            if h[node]==[]:
                return True
            visited.add(node)
            for i in h[node]:
                if not dfs(i):
                    return False
            h[node]=[]
            visited.remove(node)
            return True
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

        