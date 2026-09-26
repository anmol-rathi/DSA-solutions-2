class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        h={}
        for i,j in knowledge:
            h[i]=j
        # print(h)
        i=0
        n=len(s)
        res=''
        while i<n:
            if s[i]=='(':
                i+=1
                temp=''
                while i<n and s[i]!=')':
                    temp+=s[i]
                    i+=1
                # print(temp)
                if temp in h:
                    temp=h[temp]
                else:
                    temp='?'
                
                res+=temp
                i+=1
            else:
                res+=s[i]
                i+=1
        # print(res)
        return res




        