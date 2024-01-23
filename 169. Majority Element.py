class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        halfn=len(nums)//2
        set1=set(nums)
        for i in set1:
            if(nums.count(i)>halfn):
                return i
        