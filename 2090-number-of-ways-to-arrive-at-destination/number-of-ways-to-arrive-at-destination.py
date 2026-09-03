class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        mod=pow(10,9)+7
        h=defaultdict(list)
        dist_array=[float(inf)]*n
        for i,j,time in roads:
            h[i].append([j,time])
            h[j].append([i,time])
        heap=[]
        dist_array[0]=0
        heapq.heappush(heap,[0,0])
        ways=[0]*n
        ways[0]=1
        while heap:
            dist,node=heapq.heappop(heap)
            if dist > dist_array[node]:
                continue
            for nei,d in h[node]:
                if dist_array[nei]>(dist+d):
                    dist_array[nei]=dist+d
                    ways[nei]=ways[node] #reset ways of new shorter path
                    heapq.heappush(heap,[dist+d,nei])
                elif dist_array[nei] == (dist + d):
                    ways[nei] = (ways[nei] + ways[node]) % mod #new path jo equal h vo path ke ways add coz apna wala path equal h smallest path ke
        # print(count)
        # print(mind)
        return ways[n-1]

        

        