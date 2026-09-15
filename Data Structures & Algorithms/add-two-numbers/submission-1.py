# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode=ListNode(0)
        curr=dummyNode
        carry=0
        while l1 and l2:
            value=(l1.val+l2.val+carry)%10
            carry=(l1.val+l2.val+carry)//10
            newnode=ListNode(value)
            curr.next=newnode
            curr=curr.next
            l1=l1.next
            l2=l2.next

        while l1:
            value=(l1.val+carry)%10
            carry=(l1.val+carry)//10
            newnode=ListNode(value)
            curr.next=newnode
            curr=curr.next
            l1=l1.next

        while l2:
            value=(l2.val+carry)%10
            carry=(l2.val+carry)//10
            newnode=ListNode(value)
            curr.next=newnode
            curr=curr.next
            l2=l2.next

        if carry:
            newnode=ListNode(carry)
            curr.next=newnode
            curr=curr.next

        return dummyNode.next