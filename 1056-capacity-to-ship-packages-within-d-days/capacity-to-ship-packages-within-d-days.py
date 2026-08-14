class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def issafe(mid):
            count=0
            temp=0
            if mid<max(weights):
                return False
            for i in weights:
                temp+=i
                if temp>mid:
                    count+=1
                    temp=i
                if count>=days:
                    return False
            return True
        
        left=1
        right=sum(weights)
        while left<=right:
            mid=(left+right)//2
            if issafe(mid):
                ans=mid
                right=mid-1
            else:
                left=mid+1
        # print(ans,right,left)
        return ans



        