# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return None
        
        def checker(node,low,high):
            if not node:
                return True
            
            if not low<node.val<high:
                return False
            
            left=checker(node.left,low,node.val)
            right=checker(node.right,node.val,high)

            return left and right
        
        return checker(root,float("-inf"),float("inf"))