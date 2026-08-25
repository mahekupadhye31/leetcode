class Solution:
    def trap(self, height: List[int]) -> int:
        maxL=height[0]
        maxR=height[-1]
        left=0
        right=len(height)-1
        total=0
        while left<right:
            if maxL<maxR:
                total=total + (maxL-height[left])
                left+=1
            elif maxL>maxR:
                total=total+ (maxR-height[right])
                right-=1
            else:
                total=total + (maxL-height[left])
                left+=1
            maxL=max(maxL, height[left])
            maxR=max(maxR, height[right])
        return total