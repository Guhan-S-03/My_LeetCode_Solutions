# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        #simply we can make the sorted array of elements
        #by doing the inorder traversal and then by using the array
        #we can make the hb tree similar to 108
        sorted_array=[]

        def inorder(root):
            nonlocal sorted_array
            if not root:
                return
            inorder(root.left)
            sorted_array.append(root.val)
            inorder(root.right)
        
        def createtree(l,r):
            nonlocal sorted_array
            if l>r:
                return None
            
            m=(l+r)//2
            node=TreeNode(sorted_array[m])
            node.left=createtree(l,m-1)
            node.right=createtree(m+1,r)
            return node
        inorder(root)
        return createtree(0,len(sorted_array)-1)
        

        