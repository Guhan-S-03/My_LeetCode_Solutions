class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ##we can do the xor and right shift res to get no of ones
        #but instead we use brian kernighans to find the no of ones in the res efficiently

        xor=start ^ goal
        res=0
        while xor:
            xor = xor&(xor-1)
            res+=1
        return res

        