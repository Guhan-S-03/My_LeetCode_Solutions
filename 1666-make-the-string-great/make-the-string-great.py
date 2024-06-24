class Solution:
    def makeGood(self, s: str) -> str:
        res=""
        stack=[]

        for c in s:
            if c.isupper() and stack and stack[-1]==c.lower():
                stack.pop()
            elif c.islower() and stack and stack[-1]==c.upper():
                stack.pop()
            else:
                stack.append(c)
        
        for i in range(len(stack)):
            res+=stack[i]
        return res

        