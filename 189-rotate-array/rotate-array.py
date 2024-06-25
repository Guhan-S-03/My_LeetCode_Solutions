class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ## there is a way other than using extra array and then copy them to nums
        #simply reverse the list and then again reverse first k ele and
        #reverse the remaining ele

        def reverse(l,r):
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        
        k=k%len(nums)
        reverse(0,len(nums)-1)
        reverse(0,k-1)
        reverse(k,len(nums)-1)
        


        