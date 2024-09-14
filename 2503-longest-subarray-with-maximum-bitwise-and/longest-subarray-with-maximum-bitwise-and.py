class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ##so here we have three conditions curele>prev and curele==prev and curele<prev
        #in that equal condition is the one that going to increase our window size other two
        #conditions are going to reset our window size 

        size,res=0,0
        curmax=0

        for n in nums:
            if n>curmax:
                curmax=n
                size=1
                res=0
            elif n==curmax:
                size+=1
            else:
                size=0
            
            res=max(res,size)
        return res
        