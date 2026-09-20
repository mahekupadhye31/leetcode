import math
class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #note the values for left and right and the days_taken calculation!!!
        left=max(weights)
        right=sum(weights)
        while left<=right:
            maxcap=(left+right)//2
            days_taken=1
            total=0
            for w in weights:
                total+=w
                if total>maxcap:
                    days_taken+=1
                    total=w
            if days_taken<=days:
                right=maxcap-1
            elif days_taken>days:
                left=maxcap+1
        return left