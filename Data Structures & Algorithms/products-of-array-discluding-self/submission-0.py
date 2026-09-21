class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        prod=1
        before=[1]*n
        after=[1]*n
        output=[]

        for i in range(1,len(nums)):
            prod=prod*nums[i-1]
            before[i]=prod

        prod=1

        for i in range(len(nums)-2,-1,-1):
            prod=prod*nums[i+1]
            after[i]=prod
        
        for i in range(n):
            output.append(after[i]*before[i])
        return output
