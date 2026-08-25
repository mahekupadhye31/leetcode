class Solution:
    def integerBreak(self, n: int) -> int:
        dp=[float('-inf') for _ in range(n+1)]
        if n==1 or n==2:
            return 1
        dp[0]=dp[1]=1
        dp[3]=2
        for i in range(4,n+1):
            for j in range(1,i):
                dp[i]=max(dp[i],j*max(i-j,dp[i-j]))
        return dp[n]

