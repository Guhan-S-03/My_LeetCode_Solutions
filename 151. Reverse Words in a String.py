class Solution:
    def reverseWords(self, s: str) -> str:
        list1=s.split()
        list1=list1[::-1]
        strr=" ".join(list1)
        return strr
        