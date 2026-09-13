class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n=len(img1)
        arr1=[]
        arr2=[]
        for i in range(n):
            for j in range(n):
                if img1[i][j]==1:
                    arr1.append([i,j])
                if img2[i][j]==1:
                    arr2.append([i,j])
        
        h={}
        if not arr1 or not arr2:
            return 0
        for row,col in arr1:
            for row2,col2 in arr2:
                drow=row2-row
                dcol=col2-col
                if (drow,dcol) not in h:
                    h[(drow,dcol)]=1
                else:
                    h[(drow,dcol)]+=1
        return max(h.values())

        