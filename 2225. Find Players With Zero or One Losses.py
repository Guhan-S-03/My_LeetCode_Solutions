class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        list1=[]
        sub1=[]
        sub2=[]
        win={}
        lose={}
        for match in matches:
            if(match[0] not in win.keys()):
                win[match[0]]=1
            else:
                win[match[0]]+=1
            if(match[1] not in lose.keys()):
                lose[match[1]]=1
            else:
                lose[match[1]]+=1
        for k,v in win.items():
            if(k not in lose.keys()):
                sub1.append(k)
        for k,v in lose.items():
            if(v==1):
                sub2.append(k)
        sub1.sort()
        sub2.sort()
        list1.append(sub1)
        list1.append(sub2)
        return list1


        