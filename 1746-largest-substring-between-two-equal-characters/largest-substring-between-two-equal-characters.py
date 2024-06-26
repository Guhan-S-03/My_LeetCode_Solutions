class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        ##set method but here we are using a hashmap to store prev indx
        #and calc inbetween length

        hashmap=defaultdict(int)
        res=-1

        for i,c in enumerate(s):
            if c in hashmap:
                res=max(res,i-hashmap[c]-1)
            else:
                hashmap[c]=i
        return res

        