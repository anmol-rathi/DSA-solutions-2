class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        h={2:['a','b','c'],3:['d','e','f'], 4:['g','h','i'], 5:['j','k','l'], 6:['m','n','o'], 7:['p','q','r','s'], 8:['t','u','v'],9:['w','x','y','z']}
        def com(i,s):
            if i==len(digits):
                res.append(s)
                return
            for j in h[int(digits[i])]:
                com(i+1,s+j)
        res=[]
        com(0,'')
        # print(res)
        return res
            