class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        ##let us take an example of r,b,g balls and 3bowls
        ##if every bowl should contain equal no of rgb balls
        #then the tot no of r,g,b each should be divided by 3
        #same rule here qst is whether it is distributable or not

        hashmap=defaultdict(int)##freq

        for w in words:
            for c in w:
                hashmap[c]+=1

        for c in hashmap:
            if hashmap[c]%len(words):
                return False
        return True
        