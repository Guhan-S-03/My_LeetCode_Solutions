class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if(len(word1)!=len(word2)):
            return False
        list1=[0]*26
        list2=[0]*26
        for i in word1:
            list1[ord(i)-ord('a')]+=1
        for j in word2:
            list2[ord(j)-ord('a')]+=1
        for i in range(26):
            if((list1[i]==0 and list2[i]!=0 ) or (list1[i]!=0 and list2[i]==0 )):
                return False
        list1.sort()
        list2.sort()
        if(list1==list2):
            return True
        else:
            return False

       
        