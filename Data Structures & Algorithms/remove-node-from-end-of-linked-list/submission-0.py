# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        dummynode=ListNode(-1)
        dummynode.next=head
        fast=dummynode
        slow=dummynode

        for i in range(n):
            if fast.next:
                fast=fast.next

        while fast.next:   #when we want the fast to be at ll[-1], if we do just    fast, then on fast.next will become null
            slow=slow.next
            fast=fast.next
    
        slow.next=slow.next.next

        return dummynode.next