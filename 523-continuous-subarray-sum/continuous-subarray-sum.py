class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        #with the help of hashmap and prefixsum we can solve
        #we div the prefix by k and store the rem with ind
        #if the rem is already there then element which we added after that first seen rem are the 
        #mul of k
        #edge case 0 rem in first place
        prefix=0
        remainder={0:-1} ##rem->indx

        for i,v in enumerate(nums):
            prefix+=v
            rem=prefix % k
            if rem not in remainder:
                remainder[rem]=i
            elif i-remainder[rem]>1:
                return True
        return False
        