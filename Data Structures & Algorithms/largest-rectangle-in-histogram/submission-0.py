class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]
        maximumArea=0
        n=len(heights)
        for i,h in enumerate(heights):
            while stack and h<heights[stack[-1]]:
                j=stack.pop()
                right=i
                left=stack[-1] if stack else -1
                area=heights[j]*(right-left-1)
                maximumArea=max(maximumArea,area)
            stack.append(i)
        while stack:
            j = stack.pop()
            right = n
            left = stack[-1] if stack else -1
            width = right - left - 1
            area = heights[j] * width
            maximumArea = max(maximumArea, area)
        return maximumArea


