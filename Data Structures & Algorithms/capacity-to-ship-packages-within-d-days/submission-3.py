class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left=max(weights)
        right=sum(weights)
        minWeight=float("inf")

        while left<=right:
            mid=(left+right)//2
            total_days=1
            total_weight=0
            for w in weights:
                if total_weight+w>mid:
                    total_weight=w
                    total_days+=1
                else:
                    total_weight+=w
            if total_days>days:
                left=mid+1
            else:
                minWeight=min(minWeight,mid)
                right=mid-1      
        return minWeight