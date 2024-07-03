class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i=0

        while i<len(nums):
            if i+1<len(nums) and nums[i]==nums[i+1]:
                i+=2
            else:
                return nums[i]
        
        