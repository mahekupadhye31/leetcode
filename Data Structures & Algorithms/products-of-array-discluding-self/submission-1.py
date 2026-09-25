class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left=[1]*n
        right=[1]*n
        result=[]
        prod=1
        for i in range(1,n):
            prod=prod*nums[i-1]
            left[i]=prod
        prod=1
        for i in range(n-2,-1,-1):
            prod=prod*nums[i+1]
            right[i]=prod
        for i in range(n):
            result.append(left[i]*right[i])
        return result