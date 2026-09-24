"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new={}
        
        def clone(node):
            if node in old_to_new:
                return old_to_new[node]
            if not node:
                return None
            newnode=Node(node.val)
            old_to_new[node]=newnode

            for n in node.neighbors:
                newnode=clone(node)
                newnode.neighbors.append(clone(n))
            
            return newnode

        return clone(node)
