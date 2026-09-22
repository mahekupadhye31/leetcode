class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # the trick here is to split the first half and second half so that, we can reverse the second half of the list and have the first original one too and then we combine it
        dummynode=ListNode(0)
        dummynode.next=head
        slow=dummynode
        fast=dummynode

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        
        second_head=slow.next
        #set the end of the first LL as None
        slow.next=None
        #reverse the second LL
        prev=None
        curr=second_head
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt
        
        l1= head
        l2= prev
        take=True
        curr=dummynode
        while l1 and l2:
            if take:
                curr.next=l1
                l1=l1.next
                take= not take
            else:
                curr.next=l2
                l2=l2.next
                take= not take
            curr=curr.next
        if l1:
            curr.next=l1
        if l2:
            curr.next=l2