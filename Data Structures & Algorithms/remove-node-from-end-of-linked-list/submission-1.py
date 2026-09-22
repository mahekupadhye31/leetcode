# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummynode=ListNode(0)
        prev=dummynode
        prev.next=head
        curr=head
        fast=head
        for i in range(n):
            fast=fast.next

        while fast:
            fast=fast.next
            curr=curr.next
            prev=prev.next
        
        nxt=curr.next
        prev.next=nxt

        return dummynode.next
