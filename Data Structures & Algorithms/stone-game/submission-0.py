class Solution:
    def stoneGame(self, nums: List[int]) -> bool:
        n=len(nums)
        dp=[[-1]*(n) for _ in range(n)]
        def f(i,j):
            if i>j:
                return 0
            if i==j:
                dp[i][j]=nums[i]
                return dp[i][j]

            if dp[i][j]!=-1:
                return dp[i][j]

            take_left=nums[i]+min(f(i+2,j),f(i+1,j-1))
            take_right=nums[j]+min(f(i,j-2),f(i+1,j-1))

            dp[i][j]=max(take_left,take_right)
            return dp[i][j]
        
        alice=f(0,n-1)
        bob=sum(nums)-alice
        if alice>=bob:
            return True
        else:
            return False