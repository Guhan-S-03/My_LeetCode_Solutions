class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        pivots=[]
        less=[]
        greater=[]
        for i in nums:
            if(i<pivot):
                less.append(i)
            elif(i>pivot):
                greater.append(i)
            else:
                pivots.append(i)
        res=[]
        res=less+pivots+greater
        return res