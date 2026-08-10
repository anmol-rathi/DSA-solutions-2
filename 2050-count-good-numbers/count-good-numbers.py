class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=10**9 +7
        
        def count(x,n):
            if n==0:
                return 1
            half=count(x,n//2)
            if n%2==0:
                return half*half %mod
            else:
                return half*half*x %mod
        return count(20,n//2) * (5 if n%2==1 else 1) %mod


        