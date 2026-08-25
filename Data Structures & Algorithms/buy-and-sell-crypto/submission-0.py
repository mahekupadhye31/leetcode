class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=left+1
        mp=0
        while right<len(prices):
            if prices[left]<=prices[right]:
                mp=max(mp,prices[right]-prices[left])
                right+=1
            else:
                left+=1
                right=left+1
        return mp        
