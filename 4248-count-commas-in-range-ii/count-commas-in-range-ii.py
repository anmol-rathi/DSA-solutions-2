class Solution:
    def countCommas(self, n: int) -> int:
        res=0
        if n<1000:
            return 0
        if n==pow(10,15):
            res+=5
            n-=1
        if n>=pow(10,12):
            res+= (n-999999999999)*4
            n=999999999999
        if n>=pow(10,9):
            res+= (n-999999999)*3
            n=999999999
        #     n-= (n//temp)*(temp)
        # print((n-999999)*(2))
        if n>=pow(10,6):
            temp=pow(10,6)
            res+= ((n-999999)*(2))
            n=999999
            # n-= (n//temp)*(temp)
        if n>=pow(10,3):
            res+= (n-1000)+1
        return res