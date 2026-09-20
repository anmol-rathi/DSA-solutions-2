class Solution:
    def reverseDegree(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            temp=27-(ord(s[i])-96)
            res+= (temp*(i+1))
        return res
        