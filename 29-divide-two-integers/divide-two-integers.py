class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend==divisor:
            return 1
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1
        sign=True
        if dividend>=0 and divisor<0:
            sign=False
        if dividend<0 and divisor>0:
            sign=False
        res=0
        n=abs(dividend)
        d=abs(divisor)
        while (n>=d):
            count=0
            while (n>=(d<<(count+1))):
                count+=1
            res+=(1<<count)
            n=n-(d<<(count))
        if sign:
            return res
        else:
            return (-res)
        