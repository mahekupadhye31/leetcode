class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[[0]*(amount+1) for i in range(n)]

        for j in range(amount+1):
            if j%coins[0]==0:
                dp[0][j]=1
        
        for i in range(n):
            dp[i][0]=1
        
        for i in range(1,n):
            for j in range(1,amount+1):
                pick=0
                if j-coins[i]>=0:
                    pick=dp[i][j-coins[i]]
                notpick= dp[i-1][j]
                dp[i][j]=pick+notpick
        return dp[n-1][amount] 