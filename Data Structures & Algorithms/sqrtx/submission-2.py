class Solution:
    def mySqrt(self, x: int) -> int:
        left=1
        right=x
        while left<=right:
            mid=(left+right)//2
            ans=mid*mid
            if ans==x:
                return mid
            elif ans<x:
                left=mid+1
            else:
                right=mid-1
        return right