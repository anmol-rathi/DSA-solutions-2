class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited=set()
        city=0
        n=len(isConnected)
        for i in range(n):
            if i not in visited:
                visited.add(i)
                city+=1
                queue=deque([i])
                while queue:
                    node=queue.popleft()
                    for j,val in enumerate(isConnected[node]):
                        if val==1 and j not in visited:
                            visited.add(j)
                            queue.append(j)
        return city



        