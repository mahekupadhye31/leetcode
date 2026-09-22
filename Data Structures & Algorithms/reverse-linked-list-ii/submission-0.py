# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        curr=head
        dummynode=ListNode(0)
        dummynode.next=head
        prev1=dummynode

        for i in range(left-1):
            prev1=curr
            curr=curr.next

        section_tail=curr
        prev2=None

        for i in range(right-left+1):
            nxt=curr.next
            curr.next=prev2
            prev2=curr
            curr=nxt
            
        prev1.next=prev2
        section_tail.next=curr

        return dummynode.next
    # 1 2 3 4 5


