class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        list1=[]
        for i,word in enumerate(words):
            if(x in word):
                list1.append(i)
        return list1
        