class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack=[]
        for i in s:
            if i==')':
                temp=''
                curr=''
                while curr!='(':
                    curr=stack.pop()
                    temp+=curr
                temp=temp[:-1]
                # print(temp)
                stack.extend(temp)  
            else:
                stack.append(i)
        # print(stack)
        return ''.join(stack)   


        