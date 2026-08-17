class Solution:
    def checkValidString(self, s: str) -> bool:
        stack=[]
        power=0
        powera=0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i]==')' and stack and (stack[-1]=='('):
                stack.pop()
            elif s[i]=='*':
                power+=1
            else:
                if power>0:
                    power-=1
                else:
                    # print('hi')
                    return False
        # if len(stack)<=power:
        #     # print('hi')
        #     return True
        # # print(len(stack),power)
        # return False
        stack=[]
        power=0
        powera=0
        for i in range(len(s)-1,-1,-1):
            if s[i] == ')':
                stack.append(s[i])
            elif s[i]=='(' and stack and (stack[-1]==')'):
                stack.pop()
            elif s[i]=='*':
                power+=1
            else:
                if power>0:
                    power-=1
                else:
                    # print('hi')
                    return False
        return True
            
        