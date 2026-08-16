class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        c0=0
        c1=0
        c2=0
        for i in stones:
            if i%3==0:
                c0+=1
            elif i%3==1:
                c1+=1
            else:
                c2+=1
        d=abs(c2-c1)
        if c0%2 == 0:
            if c1>0 and c2>0:
                return True
            else:
                return False
        return d>2
        # if (c1==0 or c2==0) :
        #     return False
        # if d==0 or d==2:
        #     if c0%2==0:
        #         return True
        #     else:
        #         return False
        # if d==1 or d>2:
        #     if c0%2==0:
        #         return False
        #     else:
        #         return True
        
        