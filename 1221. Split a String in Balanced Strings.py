class Solution:
    def balancedStringSplit(self, s: str) -> int:
        maxbs=0
        rval=0
        lval=0
        for i in s:
            if(i=="R"):
                rval+=1
            elif(i=="L"):
                lval+=1
            if(rval==lval and rval!=0):
                rval=0
                lval=0
                maxbs+=1
        return maxbs
        

        