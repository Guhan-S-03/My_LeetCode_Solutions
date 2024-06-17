class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # we know that both a and b should bec less than c otherwise we will get large sum of square
        #well actually the equations say that a2,b2 <=c then we can able to add them to get tot
        #and also actual possible values of a<=root(c)

        l,r=0,int(sqrt(c))
        #we can create a array of this square values and chk but it is not req

        while l<=r:
            tot=l*l+r*r
            if tot>c:
                r-=1
            elif tot<c:
                l+=1
            else:
                return True
        return False


        