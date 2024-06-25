# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        ##actually we need to update every val by the val which is greater than them
        #so we can do inorder traversal to make them ascd but actually we can do the 
        #reverse of that reverse inorder traversal to update the global totsum
        #var and update every node and totsum val so that we can update every val from
        #right--root--left
        cursum=0

        def dfs(node):
            nonlocal cursum
            if not node:
                return 
            
            dfs(node.right)
            temp=node.val
            node.val+=cursum
            cursum+=temp
            dfs(node.left)
        dfs(root)
        return root
        