class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h={}
        for num in nums:
            h[num]=1+h.get(num,0)
        for count in list(h.values()):
            if count>1:
                return True
        return False