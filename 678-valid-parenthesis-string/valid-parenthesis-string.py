class Solution:
    def checkValidString(self, s: str) -> bool:
        #here we have wildcard and it includes 3 possibilities
        #so we have left min max range of stack sizes and check 0 is in the range 
        #if it is then true else false
        #edge case where large r>l then lmax val<0
        leftmin,leftmax=0,0

        for c in s:
            if c=="(":
                leftmin,leftmax=leftmin+1,leftmax+1
            elif c==")":
                leftmin,leftmax=leftmin-1,leftmax-1
            else:
                leftmin,leftmax=leftmin-1,leftmax+1
            if leftmax<0:
                return False
            if leftmin<0:
                leftmin=0
        return leftmin==0
        