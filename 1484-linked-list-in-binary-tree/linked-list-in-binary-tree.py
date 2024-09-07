# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def check_same(self,lnode,tnode):
        if not lnode:
            return True
        if not tnode or tnode.val!=lnode.val:
            return False
        return (
            self.check_same(lnode.next,tnode.left) or
            self.check_same(lnode.next,tnode.right)
        )

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        ## actually its similar to the another same subtree problem
        if not root:
            return False
        if self.check_same(head,root):
            return True
        return (
            self.isSubPath(head,root.left) or
            self.isSubPath(head,root.right)
        )


