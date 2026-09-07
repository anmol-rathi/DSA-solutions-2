class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod=(10**9)+7
        tot=0
        dp=[0]*26
        for c in s:
            c=ord(c)-97
            new=tot+1-dp[c]
            tot=(tot+new)%mod
            dp[c]=(dp[c]+new) %mod
        return tot
        