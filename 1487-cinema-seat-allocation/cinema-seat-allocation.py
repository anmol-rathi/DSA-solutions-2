class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        i=0
        res=0
        j=1
        reservedSeats.sort()
        while i<len(reservedSeats):
            
            s=set()
            while i<len(reservedSeats) and reservedSeats[i][0]==j:
                s.add(reservedSeats[i][1])
                i+=1
            if not s:
                res+=2
                j+=1
                continue
            if 2 not in s and 3 not in s and 4 not in s and 5 not in s:
                res+=1
                s.add(5)
            if 6 not in s and 7 not in s and 8 not in s and 9 not in s:
                res+=1
                s.add(6)
            if 4 not in s and 5 not in s and 6 not in s and 7 not in s:
                res+=1
            # print(res)
            j+=1
        res+=(n-j+1)*2
        return res
            
        # h={}
        # for i in reservedSeats:
        #     if i[0] not in h:
        #         h[i[0]]=[i[1]]
        #     else:
        #         h[i[0]].append(i[1])
        # print(h)
        # i=1
        # res=0
        # while i<=n:
        #     if i not in h:
        #         res+=2
        #         i+=1
        #         continue
        #     if 2 not in h[i] and 3 not in h[i] and 4 not in h[i] and 5 not in h[i]:
        #         res+=1
        #         h[i].append(5)
        #     if 6 not in h[i] and 7 not in h[i] and 8 not in h[i] and 9 not in h[i]:
        #         res+=1
        #         h[i].append(6)
        #     if 4 not in h[i] and 5 not in h[i] and 6 not in h[i] and 7 not in h[i]:
        #         res+=1
        #     print(res)
        #     i+=1
        # print(res)
            
        