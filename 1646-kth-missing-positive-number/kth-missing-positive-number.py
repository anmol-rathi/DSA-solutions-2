class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left=0
        if arr[left]>k:
            return k
        right=len(arr)-1
        if (arr[right]-(right+1)) < k:
            return arr[right]+ (k-(arr[right]-(right+1)))
        while right-left!=1:
            mid=(left+right)//2
            if (arr[mid]-(mid+1)) >=k:
                right=mid
            else:
                left=mid
        print(left,right)
        print(arr[left],arr[right])
        return (arr[left])+(k-((arr[left])-(left+1)))
        