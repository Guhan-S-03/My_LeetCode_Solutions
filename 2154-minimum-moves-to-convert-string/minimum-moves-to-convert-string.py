class Solution:
    def minimumMoves(self, s: str) -> int:
        min_moves=0
        i=0

        while i<len(s):
            if s[i]=='X':
                if i+1<len(s) and i+2<len(s):
                    i+=3
                    min_moves+=1
                else:
                    min_moves+=1
                    return min_moves
            else:
                i+=1
        return min_moves
            

        