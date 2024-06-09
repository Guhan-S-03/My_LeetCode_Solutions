class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        #same logic used on another prob that is subarray sum equals k
        #there we stored prefix sumand its count
        #here we need the prefix that remainder equals to the cursum remainder with k
        #so that we can remove them to get subarray thats mul of k

        res=0
        cursum=0
        prefixrem=defaultdict(int)
        prefixrem[0]=1

        for n in nums:
            cursum+=n
            rem=cursum%k
            res+=prefixrem[rem]
            prefixrem[rem]+=1
        return res

