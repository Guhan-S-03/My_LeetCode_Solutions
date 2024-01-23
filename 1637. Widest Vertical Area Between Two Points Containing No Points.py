class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:x[0])
        maxw=0
        for i in range(1,len(points)):
            width=points[i][0]-points[i-1][0]
            if(width>maxw):
                maxw=width
        return maxw


        