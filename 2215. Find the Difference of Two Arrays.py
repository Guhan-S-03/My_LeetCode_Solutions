class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        list1=set()
        list2=set()
        list3=[]
        for i in nums1:
            if(i not in nums2):
                list1.add(i)
        for j in nums2:
            if(j not in nums1):
                list2.add(j)
        list3.append(list(list1))
        list3.append(list(list2))
        return list3
        