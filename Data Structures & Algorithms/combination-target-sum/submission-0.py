class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        path=[]
        def backtrack(index):
            total=sum(path)
            if total==target:
                result.append(path[:])
                return

            if total>target or index==len(nums):
                return

            path.append(nums[index])
            backtrack(index)
            path.pop()

            backtrack(index+1)
        backtrack(0)
        return result        

