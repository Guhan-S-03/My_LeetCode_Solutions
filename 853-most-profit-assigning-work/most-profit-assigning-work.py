class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        ##actually it has two solutions one is we can create a hashmap profituptodiff with elements
        #upto max difficulty that represents the max profits for that difficulty and it has some zeros also
        #but we can fill with same logic
        #sol 2 we can sort the arrays together and sort the abilities and finding max ones

        zips=zip(difficulty,profit)
        zips=sorted(zips)
        i,best=0,0
        maxprof=0

        for ab in sorted(worker):
            while i<len(zips) and ab>=zips[i][0]:
                best=max(best,zips[i][1])
                i+=1
            maxprof+=best
        return maxprof





        