class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        #we can sort the array so that it will be easier to find duplicate
        #modification of another problm min opr to make array increasing
        #use the same greedy logic to find the min no of opr

        nums.sort()
        opr=0

        for i in range(1,len(nums)):
            prev=nums[i]
            nums[i]=max(nums[i-1]+1,nums[i])
            if nums[i]!=prev:
                opr+=(abs(nums[i]-prev))
        return opr

        