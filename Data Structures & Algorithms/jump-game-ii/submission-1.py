class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[float("inf")]*n
        dp[n-1]=0
        for i in range(n-2,-1,-1):
            for j in range(1,nums[i]+1):
                if j+i<n:
                    dp[i]=min(dp[i],1+dp[j+i])
                else:
                    continue
        return dp[0]
    
# dp[i] min no of jumps from i to the end of the game