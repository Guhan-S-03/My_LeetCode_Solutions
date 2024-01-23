class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        list1=s.split()
        word=list1[-1]
        return len(word)
        