# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# def sortList(self, head):
#     if not head or not head.next:
#         return head

#     slow = head
#     fast = head.next
#     while fast and fast.next:
#         slow = slow.next
#         fast = fast.next.next

#     mid = slow.next
#     slow.next = None

#     left = self.sortList(head)
#     right = self.sortList(mid)

#     return self.mergeTwoLists(left, right)

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1=list1
        l2=list2
        dummynode=ListNode(0)
        curr=dummynode
        while l1 and l2:
            if l1.val<=l2.val:
                curr.next=l1
                l1=l1.next
            else:
                curr.next=l2
                l2=l2.next
            curr=curr.next
        
        if l1:
            curr.next=l1
        
        if l2:
            curr.next=l2
        
        return dummynode.next

