# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        if not root:
            newNode=TreeNode(val)
            return newNode

        def insert(node,val):

            if val<node.val:
                if node.left:
                    insert(node.left,val)
                else:
                    newNode=TreeNode(val)
                    node.left=newNode

            else:
                if node.right:
                    insert(node.right,val)
                else:
                    newNode=TreeNode(val)
                    node.right=newNode
        
            return
        
        insert(root,val)
        return root
