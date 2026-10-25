# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        if p==root or q==root:
            return root

        leftCheck,rightCheck=None,None

        if root.left:
            leftCheck = self.lowestCommonAncestor(root.left,p,q)
        if root.right:
            rightCheck = self.lowestCommonAncestor(root.right,p,q)

        if leftCheck and rightCheck:
            return root
        
        if leftCheck:
            return leftCheck
        
        return rightCheck