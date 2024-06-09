class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #prefix sum and its count are stored in a hashmap
        #at every pos we sub the cursum with target and check whether the 
        #diff is already a prefix and its count is taken becoz that times we can remove
        #the prefix from cursum to get the overall target
        
        prefixsums={0:1}
        cursum=0 #prefixsum
        res=0

        for n in nums:
            cursum+=n
            diff=cursum-k
            res+=prefixsums.get(diff,0)
            prefixsums[cursum]=1+prefixsums.get(cursum,0)
        return res

        