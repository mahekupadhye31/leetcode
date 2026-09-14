# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(-1)
        l1=list1
        l2=list2
        if not l1 and l2:
            return l2
        if not l2 and l1:
            return l1
        if not l1 and not l2:
            return None

        if list1.val<=list2.val:
            dummy.next=l1
            # curr=curr1
        else:
            dummy.next=l2
            # curr=curr1
        curr=dummy
        while l1 and l2:
            if l1.val<=l2.val:
                curr.next=l1
                curr=curr.next
                l1=l1.next
            else:
                curr.next=l2
                curr=curr.next
                l2=l2.next
        
        if l1:
            curr.next=l1
            l1=l1.next
        
        if l2:
            curr.next=l2
            l2=l2.next
        
        return dummy.next
