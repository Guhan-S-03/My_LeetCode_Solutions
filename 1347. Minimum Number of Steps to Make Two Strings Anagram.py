class Solution:
    def minSteps(self, s: str, t: str) -> int:
        import collections 
        dict1 = collections.defaultdict(int)
        for i in s:
            dict1[i]+=1
        count=0
        for j in t:
            if dict1[j]:
                dict1[j]-=1
            else:
                count+=1
        return count
        