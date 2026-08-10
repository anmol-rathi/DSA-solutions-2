class Solution:
    def myAtoi(self, s: str) -> int:
        n=len(s)
        a=0
        sign=1
        for i in range(n):
            if s[i]==" ":
                continue
            if s[i]=="-":
                if i+1!=n:
                    if not s[i+1].isnumeric():
                        break
                sign=-1
                continue
            if s[i]=="+":
                if i+1!=n:
                    if not s[i+1].isnumeric():
                        break
                continue
            if s[i]=='0' and (a==None or a=='-'):
                continue
            if s[i].isnumeric():
                a=a*10 +int(s[i])
                if (sign*a)>2**31 -1:
                    return 2**31 -1
                if (sign*a)<-2**31:
                    return -2**31
                if i+1!=n:
                    if not s[i+1].isnumeric():
                        break
            if not s[i].isnumeric():
                break
        # print(a*sign)
        return a*sign

        