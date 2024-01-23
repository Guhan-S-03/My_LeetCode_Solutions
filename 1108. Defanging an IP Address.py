class Solution:
    def defangIPaddr(self, address: str) -> str:
        newstr=""
        for i in range(len(address)):
            if(address[i]=="."):
                newstr+="[.]"
            else:
                newstr+=address[i]
        return newstr
        
            

        