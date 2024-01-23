class Solution:
    def maxLength(self, arr: List[str]) -> int:
        charsett=set()

        def overlap(charsett,s):
            temp=set()
            for i in s:
                if(i in charsett or i in temp):
                    return True
                temp.add(i)
            return False
        def backtrack(i):
            if(i ==len(arr)):
                return len(charsett)

            res=0
            if not overlap(charsett,arr[i]):
                for c in arr[i]:
                    charsett.add(c)
                res=backtrack(i+1)
                for c in arr[i]:
                    charsett.remove(c)
            return max(res,backtrack(i+1))
        return backtrack(0)        