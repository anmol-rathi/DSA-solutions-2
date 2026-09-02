class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        h=defaultdict(list)
        for i,j,price in flights:
            h[i].append([j,price])
        print(h)
        heap=[]
        heapq.heappush(heap,[0,0,src])
        stops=[float('inf')]*n
        while heap:
            price,stop,node=heapq.heappop(heap)
            if node==dst:
                return price
            if stop>k or stops[node]<stop:
                continue
            stops[node]=stop
            for nei,pri in h[node]:
                heapq.heappush(heap,[price+pri,stop+1,nei])
        return -1
            
            


        