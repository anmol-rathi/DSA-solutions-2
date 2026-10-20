class Solution:
    def longestStrChain(self, words: list[str]) -> int:
        n=len(words)
        def compare(s1,s2):
            if len(s1)!=len(s2)+1:
                return False
            i=0
            j=0
            while i<len(s1):
                if j<len(s2) and s1[i]==s2[j]:
                    i+=1
                    j+=1
                else:
                    i+=1
            if i==len(s1) and j==len(s2):
                return True
            return False
        words.sort(key=len)
        # print(words)
        dp=[1]*n
        maxi=1
        for i in range(n):
            for j in range(i):
                if dp[i]<1+dp[j] and compare(words[i], words[j]):
                    dp[i]=1+dp[j]
            maxi=max(maxi,dp[i])
        return maxi