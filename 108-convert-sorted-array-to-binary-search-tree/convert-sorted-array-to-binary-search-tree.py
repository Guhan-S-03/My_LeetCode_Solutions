# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        ##since the sorted array is given to us
        #we will recursively create the tree by choosing the mid as root
        #ele lft to that as left subtree and right as right subtree

        def createtree(l,r):
            if l>r:
                return None
            
            m=(l+r)//2
            root=TreeNode(nums[m])
            root.left=createtree(l,m-1)
            root.right=createtree(m+1,r)
            return root

        return createtree(0,len(nums)-1)        