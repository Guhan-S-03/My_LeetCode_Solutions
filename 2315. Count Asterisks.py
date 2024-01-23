class Solution:
    def countAsterisks(self, s: str) -> int:
        endf=0
        count=0
        for char in s:
            if(char=="|" and endf==0):
                endf=1
            elif(char=="|" and endf==1):
                endf=0
            if(char=="*" and endf==0):
                count+=1
        return count
        