class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        minprod=nums[0]
        maxprod=nums[0]
        ans=nums[0]
        for i in range(1,n):
            temp=minprod
            minprod=min(minprod*nums[i],maxprod*nums[i],nums[i])
            maxprod=max(temp*nums[i],maxprod*nums[i],nums[i])
            ans=max(ans,maxprod)
        return ans