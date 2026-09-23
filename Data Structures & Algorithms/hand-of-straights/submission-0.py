class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        minheap = []
        count = {}

        for n in hand:
            if n not in count:
                heapq.heappush(minheap, n)
            count[n] = 1 + count.get(n, 0)

        while minheap:
            start = minheap[0]

            # Create one consecutive group
            for card in range(start, start + groupSize):
                if card not in count or count[card] == 0:
                    return False

                count[card] -= 1

                if count[card] == 0:
                    # We can only remove the smallest available card
                    if card != minheap[0]:
                        return False

                    heapq.heappop(minheap)

        return True