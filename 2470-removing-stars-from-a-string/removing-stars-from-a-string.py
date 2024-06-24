class Solution:
    def removeStars(self, s: str) -> str:
        res=""
        stack=[]

        for c in s:
            if c=="*" and stack:
                stack.pop()
            else:
                stack.append(c)
        
        for i in range(len(stack)):
            res+=stack[i]
        return res

        