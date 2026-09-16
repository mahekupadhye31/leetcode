class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i,j=0,0
        if len(nums)==1:
            return 1
        while j<len(nums):
            if j==0:
                nums[i]=nums[j]
                i+=1
                j+=1
            if nums[j]==nums[j-1]:
                j+=1
            elif nums[j]!=nums[j-1]:
                nums[i]=nums[j]
                i+=1
                j+=1
        return i


