class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total=0
        max_total=float("-inf")
        for i in range(len(nums)):
            if nums[i]>total and total<0:
                total=nums[i]
            else:
                total+=nums[i]
            max_total=max(max_total,total)
        return max_total
