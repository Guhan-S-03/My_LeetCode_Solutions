class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        ns=["0"]*len(s)
        for i in range(len(s)):
            ns[indices[i]]=s[i]
        ns="".join(ns)
        return ns