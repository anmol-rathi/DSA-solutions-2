class Solution:
    def longestValidParentheses(self, s: str) -> int:
        m=0
        left=0
        right=0
        for i in s:
            if i=='(':
                left+=1
            else:
                right+=1
            if left==right:
                m=max(m,2*left)
            elif right>left:
                left=right=0
        left=right=0
        for i in reversed(s):
            if i=='(':
                left+=1
            else:
                right+=1
            if left==right:
                m=max(m,2*left)
            elif right<left:
                right=left=0
        return m
        