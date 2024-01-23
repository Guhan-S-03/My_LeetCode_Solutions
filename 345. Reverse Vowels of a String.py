class Solution:
    def reverseVowels(self, s: str) -> str:
        list1=[]
        ss=list(map(str,s))
        vowels={"a","e","i","o","u","A","E","I","O","U"}
        for i in range(len(s)):
            if(ss[i] in vowels):
                list1.append(ss[i])
                ss[i]="_"
        list1=list1[::-1]
        for i in range(len(s)):
            if(ss[i]=="_"):
                ss[i]=list1[0]
                list1.pop(0)
        strr="".join(ss)
        return strr

        