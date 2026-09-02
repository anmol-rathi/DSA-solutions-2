class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m=len(heights)
        n=len(heights[0])
        visited=[[float("inf")]*n for _ in range(m)]
        # print(visited)
        visited[0][0]=0
        dire=[[0,-1],[-1,0],[0,1],[1,0]]
        heap=[]
        heapq.heappush(heap,[0,0,0])
        while heap:
            diff,row,col=heapq.heappop(heap)
            if row==m-1 and col==n-1:
                return diff
            for i,j in dire:
                nr=row+i
                nc=col+j
                if 0<=nr<m and 0<=nc<n:
                    ma=max(diff,abs(heights[row][col]-heights[nr][nc]))
                    if visited[nr][nc]>ma:
                        visited[nr][nc]= ma
                        heapq.heappush(heap,[ma,nr,nc])
        
