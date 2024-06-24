class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ##stack is used to store integers

        stack=[]
        res=0
        for c in operations:
            if c=="C":
                stack.pop()
            elif c=="D":
                top=stack[-1]
                top*=2
                stack.append(top)
            elif c=="+":
                top=stack[-1]
                top1=stack[-2]
                top=top+top1
                stack.append(top)
            else:
                stack.append(int(c))
        
        while stack:
            res+=stack.pop()
        return res
        