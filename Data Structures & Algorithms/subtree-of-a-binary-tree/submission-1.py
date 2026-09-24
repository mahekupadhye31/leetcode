# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p,q):
            if not p and not q:
                return True
            if (not p and q) or (p and not q) or (p.val!=q.val):
                return False
            return sameTree(p.left,q.left) and sameTree(p.right,q.right)
        
        if (not subRoot and root) or (not root and subRoot):
            return False
        
        q=deque([root])
        while q:
            node=q.popleft()
            if sameTree(node,subRoot):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False