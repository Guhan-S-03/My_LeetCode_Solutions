class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        #finding freq and compare it with chars to chk whether it can 
        #be a good one or not
        hashmap=defaultdict(int)
        for c in chars:
            hashmap[c]+=1

        res=0
        for s in words:
            hashmap1=defaultdict(int)
            flag=True
            for c in s:
                hashmap1[c]+=1
            for c in s:
                if hashmap[c]<hashmap1[c]:
                    flag=False
            if flag:
                res+=len(s)
        return res


        