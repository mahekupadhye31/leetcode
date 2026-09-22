class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1=l1
        curr2=l2
        carry=0
        dummynode=ListNode(0)
        curr=dummynode

        while curr1 and curr2:
            value=(curr1.val+curr2.val+carry)%10
            carry=(curr1.val+curr2.val+carry)//10

            newnode=ListNode(value)
            curr.next=newnode
            curr=newnode

            curr1=curr1.next
            curr2=curr2.next
        
        while curr1:
            value=(curr1.val + carry)%10
            carry= (curr1.val+carry)//10
            newnode=ListNode(value)
            curr.next=newnode
            curr=newnode
            curr1=curr1.next

        while curr2:
            value=(curr2.val + carry)%10
            carry= (curr2.val+carry)//10
            newnode=ListNode(value)
            curr.next=newnode
            curr=newnode
            curr2=curr2.next

        if carry:
            newnode=ListNode(carry)
            curr.next=newnode
            curr=newnode
        
        return dummynode.next
        


        