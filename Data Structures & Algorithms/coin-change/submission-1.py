class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[float('inf')]*(amount+1) for i in range(n)]

        #if we use coins[0] to achieve target j
        for j in range(amount+1):
            dp[0][j]= (j//coins[0]) if j%coins[0]==0 else float('inf')
        
        #if target is zero
        for i in range(n):
            dp[i][0]=0

        for i in range(1,len(coins)):
            for j in range(1,amount+1):
                taken=float("inf")
                if j-coins[i]>=0:
                    taken=1+dp[i][j-coins[i]]
                nottaken=dp[i-1][j]
                dp[i][j]=min(taken,nottaken)

        return dp[n-1][amount] if dp[n-1][amount]!=float('inf') else -1

