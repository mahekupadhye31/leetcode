class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        minimumSpeed=float('inf')
        while left<=right:
            mid=(left+right)//2
            hours=0
            for p in piles:
                if mid>p: hours+=1
                else:
                    hr=math.ceil(p/mid)
                    hours+=hr
            if hours<=h:
                right=mid-1
                minimumSpeed=min(mid,minimumSpeed)
            else:
                left=mid+1
        return minimumSpeed