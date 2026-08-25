class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        m=0
        for num in nums:
            if num-1 not in nums:
                length=0
                while num+length in nums:
                    length+=1
                    m=max(length,m)
        return m            