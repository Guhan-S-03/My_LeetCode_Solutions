class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #two sol dp and also greedy(o(n)), greedy is shifting goal towards beginning by 
        #checking cur loc

        goal=len(nums)-1

        for i in range(len(nums)-1,-1,-1):
            if (i+nums[i]>=goal):
                goal=i
        return True if goal==0 else False
        