class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        dp=[[[-1]*m for _ in range(m)] for j in range(n)]
        print(dp)
        def f(i,j1,j2):
            if j1<0 or j1>=m or j2<0 or j2>=m:
                return float('-inf')
            if dp[i][j1][j2]!=-1:
                return dp[i][j1][j2]
            if i==n-1:
                if j1==j2:
                    return grid[i][j1]
                else:
                    return grid[i][j1]+grid[i][j2]
            maxi=0
            for x in range(-1,2,1):
                for y in range(-1,2,1):
                    temp=f(i+1,j1+x,j2+y)
                    if j1==j2:
                        temp+=grid[i][j1]
                    else:
                        temp+= (grid[i][j1]+grid[i][j2])
                    maxi=max(maxi,temp)
            dp[i][j1][j2]=maxi     
            return maxi
        
        return f(0,0,m-1)
        