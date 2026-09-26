class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        current=[]
        result=[]
        used=set()

        def backtrack():
            if len(current)==n:
                result.append(current.copy())
                return
            
            for num in nums:
                if num in used:
                    continue

                current.append(num)
                used.add(num)

                backtrack()

                current.pop()
                used.remove(num)
        backtrack()
        return result