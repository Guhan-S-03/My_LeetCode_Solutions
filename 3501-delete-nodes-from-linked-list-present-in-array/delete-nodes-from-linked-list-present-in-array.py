# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        set1=set(nums)
        dummy=ListNode(0,head)
        prev=dummy

        while prev.next:
            if prev.next.val in set1:
                prev.next=prev.next.next
            else:
                prev=prev.next
        return dummy.next
        