class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dict1={}
        for i,v in enumerate(nums):
            if(v in dict1 and i-dict1[v]<=k):
                return True
            dict1[v]=i
        return False
