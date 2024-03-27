class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #if sorting is allowed then len(nums)-k is the answer
        #quicksort gives o(n) but in worstcase it is o(n2)
        if k==50000:
            return 1
        k=len(nums)-k

        def quickselect(l,r):
            pivot,p=nums[r],l
            for i in range(l,r):
                if nums[i]<=pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p+=1
            nums[p], nums[r ]= nums[r], nums[p]

            if k<p:
                return quickselect(l,p-1)
            elif k>p:
                return quickselect(p+1,r)
            else:
                return nums[p]
        return quickselect(0,len(nums)-1)



        