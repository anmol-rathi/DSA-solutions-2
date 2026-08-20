class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        visited=set()
        queue=[]
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    visited.add((i,j))
                    queue.append((i,j))
        count=0
        while queue:
            count+=1
            for i in range(len(queue)):
                row,col=queue.pop(0)
                if row+1<m and (row+1,col) not in visited:
                    queue.append((row+1,col))
                    visited.add((row+1,col))
                    mat[row+1][col]=count
                if row-1>=0 and (row-1,col) not in visited:
                    queue.append((row-1,col))
                    visited.add((row-1,col))
                    mat[row-1][col]=count
                if col+1<n and (row,col+1) not in visited:
                    queue.append((row,col+1))
                    visited.add((row,col+1))
                    mat[row][col+1]=count
                if col-1>=0 and (row,col-1) not in visited:
                    queue.append((row,col-1))
                    visited.add((row,col-1))
                    mat[row][col-1]=count
        return mat



        