class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        ##we can use a prefix sum concept here to compute prefix xors and use the left bound 
        #to eliminate the unwanted prefix sum from the right one because that contains all the xors from beginning

        prefix=[0]
        for val in arr:
            prefix.append(prefix[-1]^val)
        
        res=[]
        for l,r in queries:
            tot=prefix[r+1]
            res.append(tot^prefix[l])
        return res
        