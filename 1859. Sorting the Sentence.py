class Solution:
    def sortSentence(self, s: str) -> str:
        list1=s.split()
        lenn=len(list1)
        list2=["_"]*lenn
        for strr in list1:
            ind=int(strr[-1])-1
            list2[ind]=strr[:-1]
        sortedtxt=" ".join(list2)
        return sortedtxt
        