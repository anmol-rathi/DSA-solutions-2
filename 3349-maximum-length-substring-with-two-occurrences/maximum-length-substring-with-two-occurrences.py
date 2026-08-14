class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        h={}
        j=0
        m=0
        for i in range(len(s)):
            if s[i] not in h:
                h[s[i]]=1
            else:
                h[s[i]]+=1
                while h[s[i]]>2:
                    h[s[j]]-=1
                    j+=1
            m=max(m,i-j+1)
        return m
                    
        