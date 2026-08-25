class Solution:
    def maxArea(self, heights: List[int]) -> int:
       left=0
       n=len(heights) 
       right=n-1
       m=float('-inf')
       while left<right:
        area=min(heights[left],heights[right])*(right-left)
        m=max(area,m)
        if heights[left]<heights[right]:
            left+=1
        elif heights[left]>heights[right]:
            right-=1
        else:
            left+=1
            right-=1
       return m