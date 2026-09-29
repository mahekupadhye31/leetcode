class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        left_prod=[1]*n
        right_prod=[1]*n
        result=[1]*n
        prod=1
        for i in range(1,n):
            prod=prod*nums[i-1]
            left_prod[i]=prod
        prod=1
        for i in range(n-2,-1,-1):
            prod=prod*nums[i+1]
            right_prod[i]=prod

        for i in range(n):
            result[i]=left_prod[i]*right_prod[i]
        return result
        