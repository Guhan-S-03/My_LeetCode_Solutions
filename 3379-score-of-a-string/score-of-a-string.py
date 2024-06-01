class Solution:
    def scoreOfString(self, s: str) -> int:
        sumofascii=0

        for i in range(0,len(s)-1):
            sumofascii+=abs(ord(s[i])-ord(s[i+1]))
        return sumofascii
        