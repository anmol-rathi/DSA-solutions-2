class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        mn=s[0]
        mx=s[0]
        issorted=1
        for i in range(1,n):
            if s[i]<s[i-1]:
                issorted=0
            mn=min(mn,s[i])
            mx=max(mx,s[i])
        if issorted:
            return 0
        if n==2:
            return -1
        if s[0]==mn or s[-1]==mx:
            return 1
        for i in range(1,n-1):
            if s[i]==mn or s[i]==mx:
                return 2
        # if s[-1]==mn and s[0]==mx:
        #     return 3
        return 3