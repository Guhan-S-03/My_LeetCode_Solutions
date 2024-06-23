class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        #this prob is combination of sliding window with 
        #min and max queue becoz that is required to find whether
        #max and min element in the current window is <= limit
        #else there is no use in shifting and adding elements to the q
        #so we need to shift the left side and chk it is max or min in the 
        #any q then we need to popleft them ...

        maxq=deque()##monotonic incr
        minq=deque()##monotonic decr
        res=0
        l=0

        for r in range(len(nums)):
            #doing the things before calc max-min (updating)
            while minq and nums[r]<minq[-1]:
                minq.pop()
            while maxq and nums[r]>maxq[-1]:
                maxq.pop()
            minq.append(nums[r])
            maxq.append(nums[r])

            while maxq[0]-minq[0]>limit:
                if maxq[0]==nums[l]:
                    maxq.popleft()
                if minq[0]==nums[l]:
                    minq.popleft()
                l+=1
            res=max(res,r-l+1)
        return res

