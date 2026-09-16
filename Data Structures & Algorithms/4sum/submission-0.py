class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        result=set()

        for i in range(len(nums)):
            fixed1=nums[i]
            for j in range(i+1,len(nums)):
                fixed2=nums[j]
                left=j+1
                right=len(nums)-1
                while left<right:
                    summation=fixed1+fixed2+nums[left]+nums[right]
                    if summation==target:
                        result.add((fixed1,fixed2,nums[left],nums[right]))
                        left+=1
                        right-=1
                    elif summation<target:
                        left+=1
                    else:
                        right-=1
        return [quadriple for quadriple in result]