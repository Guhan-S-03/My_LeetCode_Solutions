class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #asusal sliding window plus greedy choice that if the prefix is neg we reset to zero
        totsub=nums[0]
        cursum=0

        for n in nums:
            if cursum<0:
                cursum=0
            cursum+=n
            totsub=max(cursum,totsub)
        return totsub
        