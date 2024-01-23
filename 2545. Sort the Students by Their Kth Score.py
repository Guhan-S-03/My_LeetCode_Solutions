class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        list1=sorted(score,key=lambda x:x[k],reverse=True)
        return list1
        