class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def find_valid_char(str,ind):
            bs=0
            while ind>=0:
                if str[ind]=='#':
                    bs+=1
                elif str[ind]!='#' and bs==0:
                    break
                else:
                    bs-=1
                ind-=1
            return ind

        inds,indt=len(s)-1,len(t)-1

        while inds>=0 or indt>=0:
            inds=find_valid_char(s,inds)
            indt=find_valid_char(t,indt)

            cs=s[inds] if inds>=0 else ""
            ct=t[indt] if indt>=0 else ""

            if cs!=ct:
                return False
            inds-=1
            indt-=1
        return True
        
        