class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m=len(grid)
        n=len(grid[0])
        if (m + n - 1) % 2 != 0 or grid[0][0] == ')' or grid[m-1][n-1] == '(':
            return False
        memo={}
        def f(i,j,count):
            # print(i,j,count)
            if i==0 and j==0 and count==0:
                return True
            if i<0 or j<0 or count<0:
                return False
            if (i,j,count) in memo:
                return memo[(i,j,count)]
            first=False
            second=False
            if grid[i-1][j]=='(':
                if count-1>=0:
                    first=f(i-1,j,count-1)
            else:
                first=f(i-1,j,count+1)
            if grid[i][j-1]=='(':
                if count-1>=0:
                    second=f(i,j-1,count-1)
            else:
                second=f(i,j-1,count+1)
            memo[(i,j,count)]=first or second    
            return first or second
        return f(m-1,n-1,1)

        