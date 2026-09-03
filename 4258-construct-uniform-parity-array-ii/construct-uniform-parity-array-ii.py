class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        nums1.sort()
        minodd=-1
        for i in nums1:
            if i%2==1:
                minodd=i
                break
        if nums1[0]%2==0 and minodd!=-1:
            return False
        return True
            