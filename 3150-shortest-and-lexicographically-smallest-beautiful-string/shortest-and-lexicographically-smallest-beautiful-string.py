class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        n = len(s)
        j = 0
        ones_count = 0
        min_len = float("inf")
        res = ""
        for i in range(n):
            if s[i] == "1":
                ones_count += 1
            
            while ones_count == k:
                
                curr_sub = s[j : i + 1]
                curr_len = len(curr_sub)
                if curr_len < min_len or (curr_len == min_len and curr_sub < res):
                    min_len = curr_len
                    res = curr_sub
                
                if s[j] == "1":
                    ones_count -= 1 
                j += 1
        return res
        
                
        