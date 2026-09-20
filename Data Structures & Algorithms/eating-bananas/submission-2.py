import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left=1
        right=max(piles)
        while left<=right:
            k=(left+right)//2
            time=0
            for p in piles:
                time+= math.ceil(p/k)
            # if time==h:
            #     return k
            if time>h:
                left=k+1
            elif time<=h:
                right=k-1
        return left
       
