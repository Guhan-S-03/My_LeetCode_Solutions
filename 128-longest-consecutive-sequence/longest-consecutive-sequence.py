class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set1 = set(nums)
        res=0

        for i in nums:
            if (i-1 not in set1):
                temp=0
                while i+temp in set1:
                    temp+=1
                res = max(res,temp)
        return res
        
                
        