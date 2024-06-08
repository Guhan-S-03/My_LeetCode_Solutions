class Solution:
    def longestValidParentheses(self, s: str) -> int:
        #every time we found close we pop and take max of prev and cur_ind - stack top
        #edge case starts with closing then we have -1 intialized on stack to handle this
        #always there will be a ind in stack 

        stack=[-1]
        lparen=0

        for i,p in enumerate(s):
            if p=="(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    lparen=max(lparen,i-stack[-1])
        return lparen



        