class Solution:
    def findMin(self, nums: List[int]) -> int:
        n=len(nums)
        left=0
        right=n-1
        while left<right:
            mid=(left+right)//2
            if nums[right]<nums[mid]:
                left=mid+1
            else:
                right=mid
        return nums[left]
        