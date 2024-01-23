class Solution:
    def sortVowels(self, s: str) -> str:
        vowlist=[]
        indlist=[]
        for i,ch in enumerate(s):
            if ch.lower() in {'a','e','i','o','u'}:
                vowlist.append(ch)
                indlist.append(i)
        flist=list(s)
        vowlist.sort()
        for i,vow in zip(indlist,vowlist):
            flist[i]=vow
        return ''.join(flist) 




        