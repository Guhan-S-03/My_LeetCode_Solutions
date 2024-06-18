class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1=set()
        intersection=set()

        for n in nums1:
            if n not in set1:
                set1.add(n)

        for n in nums2:
            if n in set1:
                intersection.add(n)
        return list(intersection)
            
        

        