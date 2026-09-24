# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        c=0 

        if not root:
            return 0
        
        def count(node,prevMax):
            nonlocal c
            if not node:
                return 0
            if node.val>=prevMax:
                c+=1
            prevMax=max(node.val,prevMax)
            count(node.left,prevMax)
            count(node.right,prevMax)
            return c

        return count(root,root.val)