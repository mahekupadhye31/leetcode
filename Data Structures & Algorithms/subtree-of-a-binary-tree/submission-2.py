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
            if (not p and q) or (not q and p) or (p.val!=q.val):
                return False
            leftcheck=sameTree(p.left,q.left)
            rightcheck=sameTree(p.right,q.right)
            return leftcheck and rightcheck
        
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
            