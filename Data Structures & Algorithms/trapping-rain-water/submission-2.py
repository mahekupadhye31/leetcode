class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        maxHeight2left=[0]*n
        maxHeight2right=[0]*n

        for i in range(1,n):
            maxHeight2left[i]=max(height[i-1],maxHeight2left[i-1])

        for j in range(n-2,-1,-1):
            maxHeight2right[j]=max(maxHeight2right[j+1],height[j+1])
        
        total=0

        for i in range(n):
            if min(maxHeight2left[i],maxHeight2right[i])>height[i]:
                total+=min(maxHeight2left[i],maxHeight2right[i])-height[i]
        return total
