# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # maxheap=[]
        # q=deque([root])
        # heapq.heappush(maxheap,-root.val)
        # while q:
        #     node=q.popleft()
        #     if node.left:
        #         q.append(node.left)
        #         heapq.heappush(maxheap,-node.left.val)
        #     if node.right:
        #         q.append(node.right)
        #         heapq.heappush(maxheap,-node.right.val)
        #     while len(maxheap)>k:
        #         heapq.heappop(maxheap)
        # return -maxheap[0]
        # result=[]
        def inorder(node):
            if not node:
                return []
            left=inorder(node.left)
            left.append(node.val)
            right=inorder(node.right)
            return left+right
        
        result= inorder(root)
        return result[k-1]
