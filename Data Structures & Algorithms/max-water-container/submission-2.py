class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left=0
        right=len(heights)-1
        maxArea=float('-inf')

        while left<right:
            width=right-left
            h=min(heights[left],heights[right])
            maxArea=max(maxArea,width*h)
            if heights[left]<=heights[right]:
                left+=1
            else:
                right-=1
        
        return maxArea