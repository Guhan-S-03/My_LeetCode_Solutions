class Solution:
    def climbStairs(self, n: int) -> int:
        list1=[0]*(n+1)
        list1[0]=1
        list1[1]=1
        for i in range(2,n+1):
            list1[i]=list1[i-1]+list1[i-2]
        return list1[-1]