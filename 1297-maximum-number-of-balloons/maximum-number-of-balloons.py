class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        #actual freq // req freq and min of that gives tot no of baloons that can be formed
        freq=Counter(text)
        balloon=Counter("balloon")

        res=len(text)#max

        for c in balloon:
            res=min(res,freq[c]//balloon[c])
        return res         