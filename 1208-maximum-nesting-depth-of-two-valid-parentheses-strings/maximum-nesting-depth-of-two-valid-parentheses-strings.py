class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        a=0
        b=0
        res=[]
        flag=True
        for i in range(len(seq)):
            if seq[i]=='(':
                if a<=b:
                    res.append(0)
                    a+=1
                    flag=True
                else:
                    res.append(1)
                    b+=1
                    flag=False
            else:
                if a==b:
                    if flag:
                        res.append(0)
                        a-=1
                    else:
                        res.append(1)
                        b-=1
                elif a>b:
                    res.append(0)
                    a-=1
                else:
                    res.append(1)
                    b-=1
        return res



        