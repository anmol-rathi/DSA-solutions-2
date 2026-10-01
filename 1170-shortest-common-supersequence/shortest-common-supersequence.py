class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n=len(str1)
        m=len(str2)
        dp=[[-1]*m for _ in range(n)]
        def f(ind1,ind2):
            if ind1 <0 or ind2<0:
                return 0
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if str1[ind1]==str2[ind2]:
                dp[ind1][ind2]=1+f(ind1-1,ind2-1)
                return dp[ind1][ind2]
            dp[ind1][ind2]=max(f(ind1-1,ind2),f(ind1,ind2-1))
            return dp[ind1][ind2]
        ind=f(n-1,m-1)
        i=n-1
        j=m-1
        # print(ind)
        # print(dp)
        s=''
        while len(s)!=m+n-ind:
            if i>=0 and j>=0:
                if str1[i]==str2[j]:
                    s+=str1[i]
                    i-=1
                    j-=1
                else:
                    val1 = dp[i - 1][j] if i - 1 >= 0 else 0
                    val2 = dp[i][j - 1] if j - 1 >= 0 else 0
                    if val1 > val2:
                        s+=str1[i]
                        i -= 1
                    else:
                        s+=str2[j]
                        j -= 1
            elif i<0:
                s+=str2[j]
                j-=1
            else:
                s+=str1[i]
                i-=1
        s=s[::-1]
        # print(s)
        return s
        # res=''
        # j=0
        # x=0
        # y=0
        # while True :
        #     if x<n and y<m and j<ind:
        #         if str1[x]==str2[y]==s[j]:
        #             res+=str1[x]
        #             x+=1
        #             y+=1
        #             j+=1
        #         elif str1[x]==s[j]:
        #             res+=str2[y]
        #             y+=1
        #         else:
        #             res+=str1[x]
        #             x+=1
        #     else:
        #         if x>=n and y<m:
        #             res+=str2[y]
        #             y+=1
        #         elif y>=m and x<n:
        #             res+=str1[x]
        #             x+=1
        #         else:
        #             break
        # # print(res)
        # return res