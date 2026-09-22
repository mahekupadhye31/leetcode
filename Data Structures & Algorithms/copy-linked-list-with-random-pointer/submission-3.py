"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        curr=head
        h={}
        #we created all the individual nodes first
        while curr:
            clone=Node(curr.val)
            h[curr]=clone
            curr=curr.next

        #add links between them
        curr=head
        while curr:
            clone=h[curr]
            if curr.next:
                clone.next=h[curr.next]
            else:
                clone.next=None
            if curr.random:
                clone.random=h[curr.random]
            else:
                clone.random=None
            curr=curr.next

        return h[head]