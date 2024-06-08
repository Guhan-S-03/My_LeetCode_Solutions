class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        #as usual sort the intervals and also iterate through the query in sorted manner
        #have a min heap and add intervals that are satisfying the current query
        #add size of the int and last range of the interval
        #there might be chance that mult q can belong to same interval so we dont pop them unnecessarily
        #we pop the unwanted int by chekcing the last range with the q
        #if dont have any satis intv then put -1 default
        intervals.sort()
        minheap=[]
        res={}#query->(ans)min size
        i=0#intervals processed
        for q in sorted(queries):
            #adding the req intrv
            while i<len(intervals) and intervals[i][0]<=q:
                l,r=intervals[i]
                heapq.heappush(minheap,(r-l+1,r))
                i+=1
            #removing the unwanted intr
            while minheap and minheap[0][1]<q:
                heapq.heappop(minheap)
            res[q]=minheap[0][0] if minheap else -1
        
        return [res[q] for q in queries]

            
        