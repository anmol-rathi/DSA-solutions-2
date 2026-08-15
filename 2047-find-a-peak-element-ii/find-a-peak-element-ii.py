class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m=len(mat)
        n=len(mat[0])
        def maxele(col):
            mm=-1
            res=-1
            for i in range(m):
                if mat[i][col]>mm:
                    mm=mat[i][col]
                    res=i
            return res
        low=0
        high=n-1
        while low<=high:
            col=(low+high)//2
            row=maxele(col)
            left = mat[row][col - 1] if col - 1 >= 0 else -1
            right = mat[row][col + 1] if col + 1 < n else -1
            if mat[row][col]>left and mat[row][col]>right:
                return [row,col]
            elif mat[row][col]<left:
                high=col-1
            else:
                low=col+1
            





        