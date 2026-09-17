class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total=sum(nums)
        if abs(target) > total:
            return 0
        # s1-s2=difference
        # s1+s2=total
        # s1=(total+difference)//2
        # difference is essentially the target (+2+2)-(2)=2
        n=len(nums)
        # we have to find no of subsets that equal to s1 
        k=(total+ target)//2
        if (total+target)%2!=0:
            return 0
        
        #dp[i][j] represents the no of subsets upto ith index in nums that are equal to j

        dp=[[0]*(k+1) for i in range(n)]

        # Initialize first row
        if nums[0] == 0:
            dp[0][0] = 2       # Assign [0] or []
        else:
            dp[0][0] = 1       # Do not select nums[0]

        if nums[0] != 0 and nums[0] <= k:
            dp[0][nums[0]] = 1

        for i in range(1,n):
            for j in range(k+1):
                pick=0
                if j-nums[i]>=0:
                    pick=dp[i-1][j-nums[i]]
                notpick=dp[i-1][j]
                dp[i][j]=pick+notpick
        
        return dp[n-1][k] if dp[n-1][k]!=0 else 0