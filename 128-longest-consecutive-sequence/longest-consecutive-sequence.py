class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num=set(nums)
        
        longest=0
        
        for i in num:
            
            if i-1 not in num:
                count=1
                a=i
                while a+1 in num:
                    count+=1
                    a+=1
                
                longest=max(longest,count)
        return longest

        