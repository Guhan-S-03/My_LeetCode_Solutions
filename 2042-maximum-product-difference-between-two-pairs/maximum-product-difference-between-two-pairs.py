class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        #sort it and diff the first two and last two
        nums.sort()
        maxdiff=abs((nums[0]*nums[1])-(nums[-1]*nums[-2]))
        return maxdiff