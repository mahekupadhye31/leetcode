class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        maxLen=float("-inf")
        for n in nums:
            if n-1 not in numSet:
                i=0
                while n+i in numSet:
                    i+=1
                    maxLen=max(maxLen,i)
        return maxLen if maxLen!=float("-inf") else 0