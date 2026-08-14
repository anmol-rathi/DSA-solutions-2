class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n=len(bloomDay)
        if m*k > n:
            return -1
        def issafe(mid):
            count=0
            temp=m
            for i in bloomDay:
                if i<=mid:
                    count+=1
                else:
                    count=0
                if count==k:
                    temp-=1
                    count=0
            if temp<=0:
                return True
            else:
                return False
        left=1
        right=max(bloomDay)
        while left<=right:
            mid=(left+right)//2
            if issafe(mid):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        return ans

        
        