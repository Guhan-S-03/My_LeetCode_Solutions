# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfspreorder(root,maxx):
            if not root:
                return 0

            res = 1 if root.val>=maxx else 0
            maxx=max(maxx,root.val)
            res+=dfspreorder(root.left,maxx)
            res+=dfspreorder(root.right,maxx)
            return res
        return dfspreorder(root,root.val)     