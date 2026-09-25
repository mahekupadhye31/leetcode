class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)

        while left<=right:
            mid=(left+right)//2
            days_taken=1
            total=0
            for w in weights:
                total+=w
                if total>mid:
                    days_taken+=1
                    total=w
            if days_taken>days:
                left=mid+1
            else:
                right=mid-1
        return left
