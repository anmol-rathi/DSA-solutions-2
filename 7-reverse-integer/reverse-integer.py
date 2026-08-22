class Solution:
    def reverse(self, x: int) -> int:
        sign=-1 if x<0 else 1
        x=x*sign
        s=str(x)
        # print(s)
        b=str()
        for i in range(len(s)-1,-1,-1):
            # print(s[i])
            b+=s[i]
        # print(b)
        c=int(b)*sign
        MIN_INT, MAX_INT = -2**31, 2**31 - 1
        return c if MIN_INT <= c <= MAX_INT else 0
        