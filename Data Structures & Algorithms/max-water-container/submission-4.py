class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        left=0
        right=n-1
        maxArea=float("-inf")

        while left<right:
            width=right-left
            height=min(heights[right],heights[left])
            maxArea=max(maxArea,width*height)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return maxArea