class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cstr=0
        for word in words:
            valid=1
            for char in word:
                if(char not in allowed):
                    valid=0
                    break
            if valid:
                cstr+=1
        return cstr
        