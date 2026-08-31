class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        result=[0]*len(temperatures)
        for i,temp in enumerate(temperatures):
            while stack and temp>temperatures[stack[-1]]:
                j=stack.pop()
                days=i-j
                result[j]=days
            stack.append(i)
        return result

        