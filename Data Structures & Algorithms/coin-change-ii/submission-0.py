class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp=[[0]*(amount+1) for i in range(n)]

        #if we use coins[0] to achieve target j
        for j in range(amount+1):
            dp[0][j]= 1 if j%coins[0]==0 else 0

        #if target is zero, then theres one combination to achieve it, by 'notpick'
        for i in range(n):
            dp[i][0]=1

        for i in range(1,len(coins)):
            for j in range(1,amount+1):
                taken=0
                if j-coins[i]>=0:
                    taken=dp[i][j-coins[i]]
                nottaken=dp[i-1][j]
                dp[i][j]=taken+nottaken
        
        return dp[n-1][amount] if dp[n-1][amount]!=0 else 0