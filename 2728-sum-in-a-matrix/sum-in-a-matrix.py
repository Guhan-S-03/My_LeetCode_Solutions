class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        ##sort the rows in the desc order and then just pick the max val at the cols
        #for each cols thats it
        rows,cols=len(nums),len(nums[0])
        for row in nums:
            row.sort(reverse=True)
        score=0
        for c in range(cols):
            maxv=-1
            for r in range(rows):
                maxv=max(maxv,nums[r][c])
            score+=maxv
        return score




        