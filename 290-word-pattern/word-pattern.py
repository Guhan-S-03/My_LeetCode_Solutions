class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        hashmap={}
        arr1=list(map(str,pattern))
        arr2=s.split(" ")
        if len(arr1)!=len(arr2):
            return False
        
        for i in range(len(arr1)):
            if arr1[i] not in hashmap:
                if arr2[i] not in hashmap.values():
                    hashmap[arr1[i]]=arr2[i]
                else:
                    return False
            else:
                if arr2[i]==hashmap[arr1[i]]:
                    continue
                else:
                    return False
        return True
            


        