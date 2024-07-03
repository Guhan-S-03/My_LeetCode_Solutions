class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        ##actually first time i solved it using a while loop
        #but they want it in a logn time so obviously binary search
        #the key here is the target has diff values on both sides
        #so we can make use of it chk mid and shift over to the side which has odd ele
        #becoz only one odd target here

        l,r=0,len(nums)-1

        while l<=r:
            m=l+((r-l)//2) ##difference of r-l so no out of bounce

            #since the target may be in first and lst pos
            if (m-1<0 or nums[m]!=nums[m-1]) and (m+1==len(nums) or nums[m]!=nums[m+1]):
                return nums[m]

            left_elements= m-1 if nums[m]==nums[m-1] else m

            if left_elements % 2:
                r=m-1
            else:
                l=m+1
        

        