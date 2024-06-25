class Solution:
    def reverseWords(self, s: str) -> str:
        ##we need to move our pointer from char until reaches empty sapce
        #and at the time we can append them to result
        q=deque()
        start=-1
        i=0

        while i<len(s):
            if s[i]!=" ":
                start=i
                while i<len(s) and s[i]!=" ":
                    i+=1
                q.appendleft(s[start:i])
            else:
                i+=1
        return " ".join(q)