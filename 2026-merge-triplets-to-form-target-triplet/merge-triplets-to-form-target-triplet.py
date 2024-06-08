class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # we can remove the trip that contains anyone val > target that is useless
        #at the same time if trip is useful then we check the target at corresponding index 
        #present in the given triplet becoz we know somehow we can get that by updating

        good=set()

        for t in triplets:
            if t[0]>target[0] or t[1]>target[1] or t[2]>target[2]:
                continue
            for i,v in enumerate(t):
                if v == target[i]:
                    good.add(i)
        return len(good)==3
        