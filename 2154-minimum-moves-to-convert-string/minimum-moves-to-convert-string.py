class Solution:
    def minimumMoves(self, s: str) -> int:
        min_moves=0
        i=0

        while i<len(s):
            if s[i]=='X':
                i+=3
                min_moves+=1
            else:
                i+=1
        return min_moves
            

        