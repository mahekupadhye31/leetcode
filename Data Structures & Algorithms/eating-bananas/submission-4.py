class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        minSpeed=float("inf")

        while left<=right:
            mid=(left+right)//2
            total=0
            for p in piles:
                if math.ceil(p/mid)==0:
                    total+=1
                else:
                    total+=math.ceil(p/mid)
            if total<=h:
                minSpeed=min(minSpeed,mid)
                right=mid-1
            else:
                left=mid+1
        return minSpeed