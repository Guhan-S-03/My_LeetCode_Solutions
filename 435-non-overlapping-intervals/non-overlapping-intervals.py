class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #sort it as usual and delete the overlapping interval which has greater 
        #endval becoz that has our goal is to remove min interval plus deleting that will reduce 
        #the no of overlapping
        intervals.sort()
        res=0
        prevend=intervals[0][1]

        for start,end in intervals[1:]:
            if(start>=prevend):
                prevend=end
            else:
                res+=1
                prevend=min(prevend,end)
        return res
        