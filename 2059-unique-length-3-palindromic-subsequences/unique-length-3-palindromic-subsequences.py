class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ##here actually storing the first occurence and finding the intermediate
        #using another occurence doesnt work, so we can use another logic 
        #that consider every pos as mid and check we have same chars or not on both sides
        #using set removes the duplicates

        left=set()
        res=set()##(mid,outer)
        right=collections.Counter(s)

        for m in range(len(s)):
            right[s[m]]-=1
            if right[s[m]]==0:
                right.pop(s[m])
            
            ##we check the 26 possibilities of chars here
            for i in range(26):
                c=chr(ord('a')+i)
                if c in left and c in right:
                    res.add((s[m],c))
            left.add(s[m])
        
        return len(res)



        