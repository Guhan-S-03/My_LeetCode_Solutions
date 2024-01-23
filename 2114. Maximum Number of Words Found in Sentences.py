class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxs=0
        for sen in sentences:
            list1=sen.split()
            lenn=len(list1)
            if(lenn>maxs):
                maxs=lenn
        return maxs
        