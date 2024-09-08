# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        n=0
        curr=head
        while curr:
            curr=curr.next
            n+=1
        baselen,rem=n//k,n%k
        res=[]

        curr=head
        for i in range(k):
            res.append(curr)
            for j in range(baselen-1 +(1 if rem else 0)):
                curr=curr.next
            if rem > 0:
                rem -=1
            if curr:
                curr.next,curr=None,curr.next
        return res

        