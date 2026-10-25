# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        best=float("-inf")
        if not root:
            return 0
        def helper(node):
            nonlocal best
            if not node:
                return 0
            left=helper(node.left)
            right=helper(node.right)

            best=max(best,left+right)
            return 1+ max(left,right)

        helper(root)
        return best