class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        look=set(nums)
        maxCount=float("-inf")

        for num in nums:
            count=0
            if num-1 in look:
                continue
            # count+=1
            while num+count in look:
                count+=1
                maxCount=max(count,maxCount)
        return maxCount if maxCount!=float("-inf") else 0