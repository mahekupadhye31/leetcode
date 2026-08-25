class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=set()
        nums=sorted(nums)
        n=len(nums)
        for i in range(n):
            mid=nums[i]
            target=-mid
            left=i+1
            right=n-1
            while left<right:
                if nums[left]+nums[right]==target:
                    result.add((nums[left],nums[right],mid))
                    # putting a break here would be wrong!!!
                    left+=1
                    right-=1
                elif nums[left]+nums[right]>target:
                    right-=1
                elif nums[left]+nums[right]<target:
                    left+=1
        return list(result)