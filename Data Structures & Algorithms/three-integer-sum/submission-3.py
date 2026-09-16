class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result=set()

        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while left<right:      #we cant use the same array element twice so left<right, and left<=right, is not possible
                summation=nums[left]+nums[right]+nums[i]
                if summation<0:
                    left+=1
                elif summation>0:
                    right-=1
                else:
                    result.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
        
        return [triplet for triplet in result]