class Solution:
    def minOperations(self, nums: List[int]) -> int:
        #greedily we can choose cur val as prev+1
        opr=0
        for i in range(1,len(nums)):
            prev=nums[i] #cur unchanged val
            nums[i]=max(nums[i-1]+1,nums[i])
            if nums[i]!=prev:
                opr+=(abs(nums[i]-prev))
        return opr

        