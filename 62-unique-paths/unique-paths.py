class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total=m+n-2
        maxi=max(m,n) -1
        mini=min(m,n) -1
        res=1
        while total!=maxi:
            res*=total
            total-=1
            
        res=res/factorial(mini)
        return int(res)

        