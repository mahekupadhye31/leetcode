class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left=0
        right=len(nums)-1
        #since it contains duplicate elements we cant tell for sure which array is sorted by just comparing left, mid. because, they could be equal and even right could be equal to mid/left
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return True
            if nums[mid]==nums[left]==nums[right]:
                left+=1
                right-=1
            elif nums[mid]<=nums[right]:
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
            else:
                if nums[left]<=target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
        return False