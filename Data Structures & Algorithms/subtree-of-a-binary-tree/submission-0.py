# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        if not subroot and root:
            return True
        
        if not root and subroot:
            return False

        def issame(p,q):
            if not p and q:
                return False

            if not q and p:
                return False

            if not p and not q:
                return True
            
            if p.val!=q.val:
                return False

            return issame(p.left,q.left) and issame(p.right,q.right)

        q=deque([root])

        while q:
            node=q.popleft()
            
            if issame(node,subroot):
                return True

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return False
            