class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        n=len(nums)
        h={}
        j=0
        maxp=0
        for i in range(n):
            if nums[i] not in h:
                h[nums[i]]=1
                # print(h[nums[i]][0])
            else:
                h[nums[i]]+=1
                    # h[nums[i]][0]=i
            while h[nums[i]] > k:
                h[nums[j]] -= 1
                j += 1       
            maxp=max(maxp,i-j+1)
        return maxp
        

        

        