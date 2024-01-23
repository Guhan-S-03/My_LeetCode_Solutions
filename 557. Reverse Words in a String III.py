class Solution:
    def reverseWords(self, s: str) -> str:
        list1=s.split()
        res=[]
        for word in list1:
            res.append(word[::-1])
        result=" ".join(res)
        return result


        