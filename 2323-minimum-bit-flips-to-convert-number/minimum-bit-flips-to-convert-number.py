class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        num=start^goal
        res=0
        while(num!=0):
            num=num&(num-1)
            res+=1
        return res
        