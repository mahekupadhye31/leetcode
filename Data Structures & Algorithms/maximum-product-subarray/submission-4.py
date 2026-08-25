class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n=len(nums)
        maxprod=minprod=nums[0]
        m=0
        if len(nums)==1:
            return nums[0]
        for i in range(1,n):
            temp=maxprod
            maxprod=max(nums[i],maxprod*nums[i],minprod*nums[i])
            minprod=min(nums[i],temp*nums[i],minprod*nums[i])
            m=max(m,maxprod,minprod)
        return m