class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        dp=[[0]*2 for _ in range(n+2)]
        dp[n][0]=dp[n][1]=0
        dp[n+1][0]=dp[n+1][1]=0
        for i in range(n-1,-1,-1):
            for j in range(0,2):
                if j==0: #buying not allowed
                    profit=max(prices[i]+dp[i+2][1],dp[i+1][0])
                else:
                    profit=max(-prices[i]+dp[i+1][0],dp[i+1][1])
                dp[i][j]=profit
        return dp[0][1]

