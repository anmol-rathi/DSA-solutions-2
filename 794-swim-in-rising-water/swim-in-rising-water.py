class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        heap=[]
        n=len(grid)
        heapq.heappush(heap,[grid[0][0],0,0])
        direction=[[-1,0],[0,1],[1,0],[0,-1]]
        res=0
        visited=set()
        while heap:
            val,row,col=heapq.heappop(heap)
            res=max(res,val)
            if row==n-1 and col==n-1:
                return res
            if (row,col) not in visited:
                visited.add((row,col))
                for i,j in direction:
                    newr=row+i
                    newc=col+j
                    if 0<=newr<n and 0<=newc<n:
                        if (newr,newc) not in visited:
                            heapq.heappush(heap,[grid[newr][newc],newr,newc])



        