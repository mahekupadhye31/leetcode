class Solution:
    def canPartition(self, arr: List[int]) -> bool:
        if sum(arr)%2!=0:
            return False
        n=len(arr)
        k=sum(arr)//2
        dp=[[False]*(k+1) for i in range(n)]
        for i in range(n):
            dp[i][0]=True
        
        for j in range(k+1):
            if arr[0]==j:
                dp[0][j]=True
        
        for i in range(1,n):
            for j in range(1,k+1):
                pick=False
                if j-arr[i]>=0:
                    pick=dp[i-1][j-arr[i]]
                notPick=dp[i-1][j]
                dp[i][j]=pick or notPick
        return dp[n-1][k]