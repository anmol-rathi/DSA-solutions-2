class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        posd=set() #row+col
        negd=set() #row-col
        board=[["."]*n for i in range(n)]
        res=[]
        def queen(r):
            if r==n:
                
                print(board)
                res.append(["".join(row) for row in board])
                return res
            for c in range(n):
                if c in col or (r+c) in posd or (r-c) in negd:
                    continue
                col.add(c)
                posd.add(r+c)
                negd.add(r-c)
                board[r][c]='Q'
                queen(r+1)
                col.remove(c)
                posd.remove(r+c)
                negd.remove(r-c)
                board[r][c]='.'
        queen(0)
        return res


                
        