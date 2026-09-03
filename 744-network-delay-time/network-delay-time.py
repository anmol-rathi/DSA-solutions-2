class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        h=defaultdict(list)
        for i,j,time in times:
            h[i].append([j,time])
        # dist=[float('inf')]*n
        # dist[k-1]=0
        visited=set()
        heap=[]
        heapq.heappush(heap,[0,k])
        while heap:
            time,node=heapq.heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            if len(visited)==n:
                return time
            # print('hi')
            for nei,t in h[node]:
                # print(nei,t)
                new_t=time+t
                heapq.heappush(heap,[new_t,nei])
        return -1



        