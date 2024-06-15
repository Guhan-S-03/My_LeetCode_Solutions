class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        #actually we can do only k projects
        #and at the same time for every k we need to choose the prjects that gives maxprofit
        #with the req for the proj should be less than equal to our current capital
        #profits added to capitals
        maxprofit=[]
        mincap=[(c,p)for c,p in zip(capital,profits)]#req cap
        heapq.heapify(mincap)

        for i in range(k):#allowed projects
            while mincap and mincap[0][0]<=w:
                c,p=heapq.heappop(mincap)
                heapq.heappush(maxprofit,-1*p)
            if not maxprofit:
                break
            w += -1 *heapq.heappop(maxprofit)
        return w
            


        