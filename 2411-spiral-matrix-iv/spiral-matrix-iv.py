# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ##it is similar to the robot simulations
        #here we can do four loops for four dir updates but instead of that we can use
        #dir to make one loop and simulate this process
        left,right=0,n
        top,bottom=0,m
        res=[[-1]*n for i in range(m)]
        directions=[[0,1],[1,0],[0,-1],[-1,0]]
        r,c,d=0,0,0

        while head:
            dr,dc=directions[d]
            while (head and (top<=r<bottom) and (left<=c<right) and res[r][c]==-1):
                res[r][c]=head.val
                head=head.next
                r,c=r+dr,c+dc
            r,c=r-dr,c-dc
            d=(d+1)%4
            dr,dc=directions[d]
            r,c=r+dr,c+dc
        return res




        