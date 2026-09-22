class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap=[]
        for i,l in enumerate(lists):
            if l!=None:
                heapq.heappush(minheap,(l.val,i,l))
        
        dummynode=ListNode(0)
        curr=dummynode

        while minheap:
            val,ind,node=heapq.heappop(minheap)

            newnode=ListNode(val)
            curr.next=newnode
            curr=newnode
            if node.next:
                heapq.heappush(minheap,(node.next.val,ind,node.next))
        
        return dummynode.next

