class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # here we are going to use maxheap and queue to store frequency becoz 
        #we care about total interval not about the characters
        count=Counter(tasks)
        maxheap=[-val for val in count.values()]
        heapq.heapify(maxheap)

        time=0
        q=deque()
        while maxheap or q:
            time+=1
            if maxheap:
                cnt = 1+heapq.heappop(maxheap)
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1]==time:
                heapq.heappush(maxheap,q.popleft()[0])
        return time


        