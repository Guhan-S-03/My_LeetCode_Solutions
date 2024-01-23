class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        alp="abcdefghijklmnopqrstuvwxyz"
        sub=[]
        for k in key:
            if(k not in sub and k!=" "):
                sub.append(k)
        subt="".join(sub)
        actmsg=""
        for m in message:
            if(m==" "):
                actmsg+=" "
            else:
                ind=subt.index(m)
                char=alp[ind]
                actmsg+=char
        return actmsg

        