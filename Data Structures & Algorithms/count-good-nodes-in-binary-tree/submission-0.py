# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0

        def check(node,prev):
            if not node:
                return False
            if node.val<prev:
                return False
            return True
            
        q=deque([(root,root.val)])

        while q:
            length=len(q)
            #prev=q[0].val
            for i in range(length):
                node,prev=q.popleft()
                if check(node,prev):
                    count+=1
                if node.left:
                    maxprev=max(node.left.val,prev)
                    q.append((node.left,maxprev))
                if node.right:
                    maxprev=max(node.right.val,prev)
                    q.append((node.right,maxprev))
                # prev=node.val
        return count
