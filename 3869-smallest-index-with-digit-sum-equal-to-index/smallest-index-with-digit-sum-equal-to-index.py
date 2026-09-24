class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def sum_digit(n):
            s=0
            while n!=0:
                a=n%10
                s+=a
                n-=a
                n=n//10
            return s
        for i in range(len(nums)):
            if i==sum_digit(nums[i]):
                return i
        return -1