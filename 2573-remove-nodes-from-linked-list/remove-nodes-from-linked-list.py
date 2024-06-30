# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #just iterating in reverse and solving the same logic 
        def reverse(root):
            prev=None
            cur=root
            while cur:
                frwd=cur.next
                cur.next=prev
                prev=cur
                cur=frwd
            return prev
        
        reverse_head=reverse(head)
        head=reverse_head
        max_val=head.val
        while head.next:
            if head.next.val<max_val:
                head.next=head.next.next
            else:
                max_val=head.next.val
                head=head.next
        return reverse(reverse_head)
        