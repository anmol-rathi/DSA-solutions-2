class Solution:
    def maxNumOfSubstrings(self, s: str) -> list[str]:
        counts = Counter(s)
        first = {c: s.find(c) for c in counts}
        last = {c: s.rfind(c) for c in counts}

        res = []
        queue = deque()

        for c in counts:
            queue.appendleft([first[c], last[c], counts[c]])

            left = inf
            right = -inf
            total = 0

            for x, y, z in queue:
                total += z
                left = min(left, x)
                right = max(right, y)

                if total == right - left + 1:
                    break

            if total == right - left + 1:
                res.append(s[left:right + 1])
                queue.clear()

        return res


# class Solution:
#     def maxNumOfSubstrings(self, s: str) -> list[str]:
#         h={}
#         for i in range(len(s)):
#             if s[i] not in h:
#                 h[s[i]]=[1,i,i]
#             else:
#                 h[s[i]][2]=i
#                 h[s[i]][0]=h[s[i]][2]-h[s[i]][1]+1
#         res=[]
#         sorted_h = dict(sorted(h.items(), key=lambda item: item[1][0]))
#         set_r=set()
#         # print(sorted_h)
#         for i in sorted_h:
#             rng,start,end=sorted_h[i]
#             temp=[]
#             flag=True
#             for j in range(start,end+1):
#                 if j not in set_r:
#                     temp.append(j)
#                 else:
#                     flag=False
#                     break
#             if flag:
#                 set_r.update(temp)
#                 res.append(s[start:end+1])
#         # print(res)
#         return res
            

            

            
                