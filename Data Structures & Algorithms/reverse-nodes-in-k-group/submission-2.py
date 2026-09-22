# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#       1 2 3 4 5 6
# 1)    6 5 4 3 2 1
# 2).  prev       head

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count=0
        prev=None
        curr=head
        for _ in range(k):
            if not curr:
                return head
            curr = curr.next
        
        curr=head

        for i in range(k):
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        
        head.next=self.reverseKGroup(curr,k)

        return prev



