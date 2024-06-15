class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        #actually we can do 2 sol in n time cmp
        #at one run we can chk it is incr or decr with two bools
        #or else we can chk only incr by reverse if it is decr

        if (nums[-1]-nums[0])<0:
            nums.reverse()
        
        for i in range(len(nums)-1):
            if not nums[i]<=nums[i+1]:
                return False
        return True