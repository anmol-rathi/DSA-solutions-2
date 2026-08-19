class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=Counter(tasks)
        maxheap=[]
        for i in count:
            maxheap.append(-(count[i]))
        heapq.heapify(maxheap)
        time=0
        queue=deque()
        while maxheap or queue:
            time+=1
            if maxheap:
                a=heapq.heappop(maxheap)
                a+=1
                if a!=0:
                    queue.append((a,time+n))        
            if queue and queue[0][1]==time:
                heapq.heappush(maxheap,queue.popleft()[0])
        return time

