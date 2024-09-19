class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        ## so here we can find all the possibilities by splitting over every operator 
        #because every opr has lft and right part that takes their own backtrack to find
        #all the possible outcomes(every backtrack call has a window in which all the 
        #possible res are calculated)

        operators={
            '+': lambda x,y:x+y,
            '-': lambda x,y:x-y,
            '*': lambda x,y:x*y
        }

        def backtrack(left,right):
            res=[]
            for i in range(left,right+1):
                if expression[i] in operators:
                    leftres=backtrack(left,i-1)
                    rightres=backtrack(i+1,right)
                    for val1 in leftres:
                        for val2 in rightres:
                            res.append(operators[expression[i]](val1,val2))
            if res==[]:
                return [int(expression[left:right+1])]
            else:
                return res 
        
        return backtrack(0,len(expression)-1)
        