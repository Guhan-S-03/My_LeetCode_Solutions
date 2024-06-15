class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        hashmap=defaultdict(int)
        gpair=0
        for n in nums:
            hashmap[n]+=1
        for k in hashmap:
            n=hashmap[k]
            gpair+=(n*(n-1)//2)
        return gpair
    
        