class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        maxheight2left=[0]*n
        maxheight2right=[0]*n

        for i in range(1,len(height)):
            maxheight2left[i]=max(maxheight2left[i-1],height[i-1])
        for j in range(len(height)-2,-1,-1):
            maxheight2right[j]=max(maxheight2right[j+1],height[j+1])
        
        total=0
        for i in range(len(height)):
            h=min(maxheight2left[i],maxheight2right[i])
            if height[i]>h: 
                continue
            else:
                total=total+(h-height[i])
        return total
