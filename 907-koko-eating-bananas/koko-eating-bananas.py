class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def issafe(mid):
            temp=h
            for pile in piles:
                temp-=pile//mid
                if (pile%mid)!=0:
                    temp-=1
                if temp<0:
                    return False
            return True
        left=1
        right=max(piles)
        while left<=right:
            mid=(left+right)//2
            if issafe(mid):
                right=mid-1
            else:
                left=mid+1
        return left

            
        