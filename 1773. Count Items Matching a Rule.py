class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        cnt=0
        if(ruleKey=="type"):
            chki=0
        elif(ruleKey=="color"):
            chki=1
        else:
            chki=2
        for item in items:
            if(item[chki]==ruleValue):
                cnt+=1
        return cnt