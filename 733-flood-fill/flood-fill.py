class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue=[]
        m=len(image)
        n=len(image[0])
        visited=set()
        visited.add((sr,sc))
        queue.append((sr,sc))
        c=image[sr][sc]
        while queue:
            row,col=queue.pop(0)
            if row-1>=0 and image[row-1][col]==c and (row-1,col) not in visited:
                queue.append((row-1,col))
                visited.add((row-1,col))
                image[row-1][col]=color
            if row+1<m and image[row+1][col]==c and (row+1,col) not in visited:
                queue.append((row+1,col))
                visited.add((row+1,col))
                image[row+1][col]=color
            if col-1>=0 and image[row][col-1]==c and (row,col-1) not in visited:
                queue.append((row,col-1))
                visited.add((row,col-1))
                image[row][col-1]=color
            if col+1<n and image[row][col+1]==c and (row,col+1) not in visited:
                queue.append((row,col+1))
                visited.add((row,col+1))
                image[row][col+1]=color
        image[sr][sc]=color
        return image