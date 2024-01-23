class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        mid=len(s)//2
        lenn=len(s)
        for i in range(0,mid):
            temp=s[i]
            s[i]=s[lenn-1-i]
            s[lenn-1-i]=temp

    



        