class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        result=set()
        nums.sort()
        for i in range(len(nums)):
            num1=nums[i]
            left=i+1
            right=n-1
            while left<right:
                num2=nums[left]
                num3=nums[right]
                total=num1+num2+num3
                if total==0:
                    result.add((num1,num2,num3))
                    left+=1
                    right-=1
                elif total>0:
                    right-=1
                else:
                    left+=1
        
        return list(result)