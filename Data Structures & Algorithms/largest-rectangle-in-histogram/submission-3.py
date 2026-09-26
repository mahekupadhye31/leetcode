class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n=len(heights)
        nse=[n]*n
        pse=[-1]*n
        stack=[]
        maxArea=float("-inf")
        for i in range(n):
            while stack and heights[i]<heights[stack[-1]]:
                top=stack.pop()
                nse[top]=i
            stack.append(i)
        
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and heights[i]<heights[stack[-1]]:
                top=stack.pop()
                pse[top]=i
            stack.append(i)
        
        for i in range(n):
            maxArea=max(maxArea, heights[i]*(nse[i]-pse[i]-1))

        return maxArea