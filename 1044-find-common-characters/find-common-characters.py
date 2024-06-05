class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        dict1=Counter(words[0])

        for i in range(len(words)):
            cur_dict=Counter(words[i])
            for c in dict1:
                dict1[c]=min(dict1[c],cur_dict[c])
        res=[]
        for c in dict1:
            for i in range(dict1[c]):
                res.append(c)
        return res
        