class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        if not lists:
            return None

        for i, head in enumerate(lists):
            if not head:
                continue                              # FIX: was `return` — that exited the
                                                        # whole function on the first empty list

            heapq.heappush(minheap, (head.val, i, head))  # FIX: added `i` as a tiebreaker 

        dummyNode = ListNode(-1)
        curr = dummyNode

        while minheap:
            val, i, node = heapq.heappop(minheap)
            curr.next = node
            curr = node
            if node.next:
                heapq.heappush(minheap, (node.next.val, i, node.next))

        return dummyNode.next