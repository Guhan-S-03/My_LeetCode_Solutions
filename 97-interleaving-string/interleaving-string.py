class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #2dmatrix with bottom-up sol in which we check if true we go for right or bottom based on i,j
        if len(s1)+len(s2)!=len(s3):
            return False
        dp=[[False for j in range(len(s2)+1)]for i in range(len(s1)+1)]
        dp[len(s1)][len(s2)]=True

        for i in range(len(s1),-1,-1):
            for j in range(len(s2),-1,-1):
                if i<len(s1) and s1[i]==s3[i+j] and dp[i+1][j]:
                    dp[i][j]=True
                if j<len(s2) and s2[j]==s3[i+j] and dp[i][j+1]:
                    dp[i][j]=True
        return dp[0][0]  
        