class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n=len(s)
        def ispalindrome(s):
            len_string=len(s)
            mid=len_string//2
            last=len_string-1
            for i in range(mid):
                if (s[i]!=s[last]):
                    return False
                last-=1
            return True
        ind=0
        res=0
        while ind<n:
            if ispalindrome(s[ind:k+ind]) and len(s[ind:k+ind])>=k:
                # print(s[ind:k+ind])
                res+=1
                ind+=k
            elif ispalindrome(s[ind:k+1+ind]) and len(s[ind:k+1+ind])>=k:
                res+=1
                ind+=k+1
            else:
                ind+=1
        return res

        