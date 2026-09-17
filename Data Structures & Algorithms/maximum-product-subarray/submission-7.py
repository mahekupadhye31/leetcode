class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax=1
        currMin=1
        maxx,minn=float('-inf'),float('inf')
        for num in nums:
            temp=currMax 
            currMax=max(num*currMin, num*currMax, num) 
            currMin=min(num*currMin, num*temp, num) 
            maxx=max(currMax,maxx) 
            minn=min(currMin,minn) 
    
        return maxx