class Solution:
    def interpret(self, command: str) -> str:
        outs=""
        n=len(command)
        i=0
        while(i<n):
            if(command[i]=="G"):
                outs+="G"
                i+=1
            elif(command[i]=="(" and command[i+1]==")"):
                outs+="o"
                i+=2
            else:
                outs+="al"
                i+=4
        return outs
