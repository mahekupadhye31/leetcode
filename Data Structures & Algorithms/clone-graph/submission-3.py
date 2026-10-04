"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        oldtonew={}
        def clone(node):
            if node in oldtonew:
                return oldtonew[node]
            nn=Node(node.val)
            oldtonew[node]=nn
            for neighbor in node.neighbors:
                nn.neighbors.append(clone(neighbor))
            return nn
        return clone(node)
        