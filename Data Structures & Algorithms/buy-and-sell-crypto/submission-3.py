class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left=0
        right=1
        n=len(prices)
        profit=float("-inf")

        while right<n and left<n:
            if prices[right]>prices[left]:
                profit=max(profit, prices[right]-prices[left])
                right+=1
            else:
                left+=1
                right=left+1
        
        return profit if profit!=float("-inf") else 0