class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        slist=list(map(str,s.split()))
        nlist=slist[:k]
        jstr=' '.join(nlist)
        return jstr
        