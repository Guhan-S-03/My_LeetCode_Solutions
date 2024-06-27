class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        #the qst is for any k students so we can sort them
        nums.sort()
        l=0
        mindiff=max(nums)
        for r in range(k-1,len(nums)):
            diff=nums[r]-nums[l]
            mindiff=min(mindiff,diff)
            l+=1
        return mindiff

        