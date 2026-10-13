class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n=len(nums)
        j=0
        while j<n:
            for i in range(n-1):
                a=nums[i]
                b=nums[i+1]
                if a>b:
                    nums[i],nums[i+1]=nums[i+1],nums[i]
            j+=1
        return nums 