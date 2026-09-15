class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev = None
        curr = slow.next
        slow.next = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        dummy = ListNode(-1)
        start = dummy
        first = head
        second = prev
        boolean = True

        while first and second:
            if boolean:
                start.next = first
                first = first.next
            else:
                start.next = second
                second = second.next
            start = start.next
            boolean = not boolean

        if first:                # NEW: attach whatever's left of the first half
            start.next = first

        