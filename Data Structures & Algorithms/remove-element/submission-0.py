class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n=len(nums)
        count=0
        j=0
        for i in range(n):
            if nums[i]==val:
                count+=1
            else:
                nums[j]=nums[i]
                j+=1
        return n-count