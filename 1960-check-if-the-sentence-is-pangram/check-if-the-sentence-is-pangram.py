class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        hashmap=defaultdict(int)

        for c in sentence:
            hashmap[c]+=1
        keys=hashmap.keys()
        if len(keys)==26:
            return True
        else:
            return False
       