class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        ##we know that the first and last timep diff should be on the outer side 
        #because the inner diff is obviously higher
        #thats the key point here

        timePoints.sort()
        def tp_to_min(tp):
            h,m=map(int,tp.split(":"))
            return (h*60)+m

        res=(24*60)-(tp_to_min(timePoints[-1]))+(tp_to_min(timePoints[0]))

        for i in range(len(timePoints)-1):
            cur=tp_to_min(timePoints[i+1])
            prev=tp_to_min(timePoints[i])
            diff=cur-prev
            res=min(res,diff)
        return res
        