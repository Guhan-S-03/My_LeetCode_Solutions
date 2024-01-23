class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x=0
        for string in operations:
            if('+'in string):
                x+=1
            elif('-'in string):
                x-=1
        return x
        