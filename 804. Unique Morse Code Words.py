class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alp="abcdefghijklmnopqrstuvwxyz"
        unique=set()
        for word in words:
            mcode=""
            for char in word:
                ind=alp.index(char)
                mors=morse[ind]
                mcode+=mors
            unique.add(mcode)
        return len(unique)

        