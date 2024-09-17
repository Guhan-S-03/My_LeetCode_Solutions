class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        ##here i am using the dict approach to solve this 

        hashmap={}

        for w in s1.split(" ")+s2.split(" "):
            if w not in hashmap:
                hashmap[w]=0
            hashmap[w]+=1
        
        res=[]
        for k,v in hashmap.items():
            if v==1:
                res.append(k)
        return res

        