class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alp="abcdefghijklmnopqrstuvwxyz"
        for al in alp:
            if(sentence.count(al)==0):
                return False
        return True
       